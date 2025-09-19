import wx
import requests
import json
import os
import re
import threading
import subprocess
from urllib.parse import quote
import my_mainform

# 使用 wx.CallAfter 来安全地从后台线程更新主GUI线程
from wx.lib.pubsub import pub


class SubtitleDownloaderFrame(my_mainform.mainFrame):
    def __init__(self):
        super().__init__(None)

        
        # ---- 查询结果列表 ----
        self.result_list.InsertColumn(0, "查询内容", width=200)
        self.result_list.InsertColumn(1, "字幕名称", width=200)
        self.result_list.InsertColumn(2, "语言", width=60)
        self.result_list.InsertColumn(3, "时长", width=80)
        self.result_list.InsertColumn(4, "下载链接", width=300) # 隐藏真实链接，仅用于内部数据存储

        # ---- 状态栏 ----
        self.status_bar.SetStatusWidths([-4, -1])   
        self.SetStatusText("准备就绪")
        self.SetStatusText("窗口未置顶", 1)

        self.dir_input.SetValue(r"A:\downing")
        self.reset_button.Disable()

        # 内部数据存储
        self.search_content = ""
        self.search_results_data = []

        # ---- PubSub 订阅，用于线程安全地更新UI ----
        pub.subscribe(self.update_status, "update_status")
        pub.subscribe(self.update_list, "update_list")
        # pub.subscribe(self.show_message_dialog, "show_message")

    def update_status(self, message):
        """线程安全地更新状态栏"""
        self.SetStatusText(message)

    def update_list(self, data):
        """线程安全地更新列表内容"""
        self.result_list.DeleteAllItems()
        self.search_results_data = data
        for index, item in enumerate(self.search_results_data):
            languages = "&".join(item.get('languages', []))
            duration = self._format_duration(item.get('duration', 0))
            self.result_list.InsertItem(index, self.search_content)
            self.result_list.SetItem(index, 1, item.get('name', ''))
            self.result_list.SetItem(index, 2, languages if languages else '')
            self.result_list.SetItem(index, 3, duration)
            self.result_list.SetItem(index, 4, item.get('url', ''))

    def _format_duration(self, duration_ms):
        """
        将毫秒时间转换为 HH:MM:SS 格式
        
        Args:
            duration_ms (int): 以毫秒为单位的时间长度
            
        Returns:
            str: 格式化后的时间字符串 HH:MM:SS
        """
        # 将毫秒转换为秒
        total_seconds = int(duration_ms) // 1000
        
        # 计算小时、分钟和秒
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
    
        # 格式化为 HH:MM:SS
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def _match_av(self, text):
        # 去除windows路径中的非法字符：
        text = re.sub(r'[\\/:*?"<>|]', '', text)

        youma_pattern = re.compile(r'((?:\d{3})?[a-z]{2,5})[-_\s]?([\d]{2,5})(.*)$', re.IGNORECASE)  # 忽略大小写
        fc_pattern = re.compile(r'(FC[2]?[-_\s]?(?:PPV)?)[-_\s]?(\d{7})(.*)$', re.IGNORECASE)
        p_lst = [fc_pattern, youma_pattern]
        match = None
        for pattern in p_lst:
            match = pattern.search(text)
            if match:
                sn = f"{match.group(1)}-{match.group(2)}"
                return sn.strip().upper(), f"{match.group(3)}".strip()
        if not match:
            return None, text.strip()     # 未匹配时返回None和整个字符串
        
    def on_create_dir( self, event ):
        save_dir = self.dir_input.GetValue()
        if not save_dir:
            wx.MessageBox("请先选择保存目录！", "提示", wx.OK | wx.ICON_INFORMATION)
            return
        
        new_folder = self.name_input.GetValue()
        sn,name = self._match_av(new_folder)
        if not self.is_av.GetValue() or not sn:
            # 去除windows路径中的非法字符：
            new_folder = re.sub(r'[\\/:*?"<>|]', '', new_folder)

        else:
            extend = ''
            if self.is_4k.IsChecked():
                extend = '4K'
            if self.is_crack.IsChecked():
                extend += 'U'
            if self.is_leaked.IsChecked():
                extend += 'L'
            if self.is_enhance.IsChecked():
                extend += 'E'
            if self.is_cn.IsChecked():
                extend += 'C'
            new_folder = sn + '-' + extend + ' '+ name 

        if new_folder:
            try:
                name_folder_path = os.path.join(save_dir, new_folder)
                os.makedirs(name_folder_path, exist_ok=True)
                self.dir_input.SetValue(name_folder_path)
                self.status_bar.SetStatusText(f"已创建新文件夹为：{new_folder}")
                self.reset_button.Enable()
            except Exception as e:
                self.status_bar.SetStatusText(f"创建文件夹失败：{e}")

    def on_reset(self, event):
        self.name_input.SetValue("")
        # 获取当前目录值
        current_dir = self.dir_input.GetValue()
        # 获取父目录
        parent_dir = os.path.dirname(current_dir)
        self.dir_input.SetValue(parent_dir)
        self.reset_button.Disable()
        self.SetStatusText("准备就绪")
        

    def on_top_window( self, event ):
        if self.status_bar.GetStatusText(1)=="窗口未置顶":
            self.SetWindowStyle(self.GetWindowStyle() | wx.STAY_ON_TOP)
            self.status_bar.SetStatusText("窗口已置顶", 1)

        else:
            self.SetWindowStyle(self.GetWindowStyle() & ~wx.STAY_ON_TOP)
            self.status_bar.SetStatusText("窗口未置顶", 1)


    def on_open_dir( self, event ):
        dir_path = self.dir_input.GetValue()
        if dir_path and os.path.exists(dir_path):
            try:
                subprocess.Popen(f'explorer "{self.dir_input.GetValue()}"')
            except Exception as e:
                wx.MessageBox(f"无法打开目录：{str(e)}", "错误", wx.OK | wx.ICON_ERROR)
        else:
            self.status_bar.SetStatusText("警告：请先确认保存目录是否有效！")

    def on_browse(self, event):
        """处理“浏览”按钮点击事件，打开文件夹选择对话框"""
        dialog = wx.DirDialog(self, "选择保存文件夹", style=wx.DD_DEFAULT_STYLE)
        if dialog.ShowModal() == wx.ID_OK:
            self.dir_input.SetValue(dialog.GetPath())
        dialog.Destroy()

    def on_search(self, event):
        """处理“查询”按钮点击事件"""
        name = self.name_input.GetValue().strip()
        if not name:
            wx.MessageBox("请输入要查询的字幕名称！", "提示", wx.OK | wx.ICON_INFORMATION)
            return
        
        if self.is_av.IsChecked():
            sn, others = self._match_av(name)
            if sn:
                name = sn

        self.SetStatusText(f"正在查询 '{name}'...")
        self.search_content = name
        # 在新线程中执行查询，避免UI卡顿
        threading.Thread(target=self._search_thread, args=(name,)).start()

    def _search_thread(self, name):
        """查询字幕的后台线程"""
        # 对URL中的中文字符和特殊字符进行编码
        api_url = f"http://api-shoulei-ssl.xunlei.com/oracle/subtitle?name={quote(name)}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        try:
            response = requests.get(api_url, headers=headers, timeout=10)
            response.raise_for_status()  # 如果请求失败 (如 404, 500)，则抛出异常
            
            data = response.json()
            if data.get('code') == 0 and 'data' in data:
                subtitles = data['data']
                wx.CallAfter(pub.sendMessage, "update_list", data=subtitles)
                wx.CallAfter(pub.sendMessage, "update_status", message=f"查询成功，找到 {len(subtitles)} 条结果")
            else:
                wx.CallAfter(pub.sendMessage, "update_status", message=f"查询失败: {data.get('result', '未知错误')}")
                

        except requests.exceptions.RequestException as e:
            wx.CallAfter(pub.sendMessage, "update_status", message="查询失败：网络错误")
        except json.JSONDecodeError:
            wx.CallAfter(pub.sendMessage, "update_status", message="查询失败：响应格式错误")

    def on_download_selected(self, event):
        """处理“下载选中字幕”按钮点击事件"""
        save_dir = self.dir_input.GetValue()
        if not save_dir:
            wx.MessageBox("请先选择保存目录！", "提示", wx.OK | wx.ICON_INFORMATION)
            return
        
        selected_items = self._get_selected_list_items()
        if not selected_items:
            wx.MessageBox("请至少选择一个要下载的字幕！", "提示", wx.OK | wx.ICON_INFORMATION)
            return

        self.SetStatusText(f"开始下载 {len(selected_items)} 个文件...")
        # 在新线程中执行下载
        threading.Thread(target=self._download_thread, args=(selected_items, save_dir)).start()
        
    def on_batch_download(self, event):
        """处理“批量下载”按钮点击事件"""
        save_dir = self.dir_input.GetValue()
        if not save_dir:
            wx.MessageBox("请先选择保存目录！", "提示", wx.OK | wx.ICON_INFORMATION)
            return
        
        if not self.search_results_data:
            wx.MessageBox("请先查询字幕，再进行批量下载！", "提示", wx.OK | wx.ICON_INFORMATION)
            return

        count_to_download = self.batch_count_spin.GetValue()
        
        # 按照优先级排序：简体 -> 繁体 -> 其他
        sorted_results = sorted(self.search_results_data, key=lambda x: self._get_language_priority(x.get('languages', [])))
        
        items_to_download = sorted_results[:count_to_download]
        
        if not items_to_download:
            self.SetStatusText("没有可供批量下载的字幕。")
            return
            
        self.SetStatusText(f"开始批量下载 {len(items_to_download)} 个文件...")
        threading.Thread(target=self._download_thread, args=(items_to_download, save_dir)).start()

    def _get_language_priority(self, languages):
        """为语言列表分配优先级，用于排序"""
        if '简体' in languages:
            return 0
        if '繁体' in languages:
            return 1
        # 假设"英文"或其他非中文语言优先级较低
        if '英语' in languages:
            return 3
        return 2 # 其他/未知语言

    def _get_selected_list_items(self):
        """获取ListCtrl中所有被选中的项目对应的数据"""
        selected_items_data = []
        selected_index = -1
        while True:
            selected_index = self.result_list.GetNextItem(selected_index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
            if selected_index == -1:
                break
            selected_items_data.append(self.search_results_data[selected_index])
        return selected_items_data
        
    def _download_thread(self, items_to_download, save_dir):
        """下载文件的后台线程"""
        success_count = 0
        fail_count = 0
        
        for i, item in enumerate(items_to_download):
            url = item.get('url')
            filename = item.get('name', f"subtitle_{i}.srt").replace("/", "_").replace("\\", "_") # 避免路径字符
            
            if not url or not filename:
                fail_count += 1
                continue

            # 检查文件后缀，如果为空则添加默认的.srt后缀
            if not os.path.splitext(filename)[1]:
                filename += ".srt"

            # 处理文件名冲突
            filepath = os.path.join(save_dir, filename)
            counter = 1
            base, ext = os.path.splitext(filepath)
            while os.path.exists(filepath):
                filepath = f"{base} ({counter}){ext}"
                counter += 1
            
            wx.CallAfter(pub.sendMessage, "update_status", message=f"正在下载 {filename}...")
            
            try:
                r = requests.get(url, stream=True, timeout=15)
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                success_count += 1
            except requests.exceptions.RequestException:
                fail_count += 1
                # 可以在这里记录下载失败的日志
        
        final_message = f"下载完成！成功 {success_count} 个，失败 {fail_count} 个。"
        wx.CallAfter(pub.sendMessage, "update_status", message=final_message)

if __name__ == '__main__':
    app = wx.App(False)
    frame = SubtitleDownloaderFrame()
    frame.Show()
    app.MainLoop()
