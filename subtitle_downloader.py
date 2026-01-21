# -*- coding: utf-8 -*-

import os
import re
import threading
import subprocess
import requests
from urllib.parse import quote
import ttkbootstrap as ttk
# 显式引入 tkinter 常量，防止版本兼容性问题
from tkinter.constants import *
from tkinter import filedialog, messagebox

try:
    import win32com.client
    HAS_WIN32COM = True
except ImportError:
    HAS_WIN32COM = False
    print("Warning: pywin32 not found, 'Open Dir' feature may be limited.")


# 启用高 DPI 感知（Windows）
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# ###########################################################################
# Class SubtitleDownloaderFrame
# ###########################################################################

class SubtitleDownloaderFrame(ttk.Window):
    def __init__(self):
        self.theme_var = "litera"
        super().__init__(title="字幕查询下载工具 - liug", themename=self.theme_var)
        # super().__init__(title="字幕查询下载工具 - liug", themename="litera")
        
        # 窗口居中与大小设置
        # 稍微加宽窗口以容纳新增的“查询内容”和“下载链接”列
        self.geometry("1300x900") 
        self.position_center()

        # ------------------ 1. 优先定义所有UI变量 ------------------
        self.name_var = ttk.StringVar()
        self.dir_var = ttk.StringVar(value=r"A:\downing")
        self.batch_count_var = ttk.IntVar(value=5)
        
        self.is_av_var = ttk.BooleanVar(value=True)
        self.is_4k_var = ttk.BooleanVar(value=False)
        self.is_crack_var = ttk.BooleanVar(value=False)
        self.is_lada_var = ttk.BooleanVar(value=True)
        self.is_enhance_var = ttk.BooleanVar(value=False)
        self.is_leaked_var = ttk.BooleanVar(value=False)
        self.is_cn_var = ttk.BooleanVar(value=True)

        self.search_results_data = []
        self.search_content = ""  # 用于存储当前查询的内容
        self.topmost_flag = False
        
        self.status_left_var = ttk.StringVar(value="准备就绪")
        self.status_right_var = ttk.StringVar(value="双击置顶窗口")

        # ------------------ 2. 初始化界面 ------------------
        self._init_ui()
        self._setup_listview()

    def _init_ui(self):
        """初始化界面布局"""
        # 主容器，添加一些内边距
        main_container = ttk.Frame(self, padding=10)
        main_container.pack(fill=BOTH, expand=YES)

        # ------------------ 上部分：文件目录设置 ------------------
        dir_group = ttk.LabelFrame(main_container, text=" 文件目录设置 ", padding=15)
        dir_group.pack(fill=X, pady=(0, 10))

        # 1. 片名输入行
        input_frame = ttk.Frame(dir_group)
        input_frame.pack(fill=X, pady=(0, 10))
        
        ttk.Label(input_frame, text="片名:", width=8).pack(side=LEFT)
        name_entry = ttk.Entry(input_frame, textvariable=self.name_var, bootstyle="info")
        name_entry.pack(side=LEFT, fill=X, expand=True, padx=5)
        name_entry.bind('<Return>', lambda e: self.on_search())
        
        ttk.Button(input_frame, text="重置", bootstyle="danger-outline", width=10, command=self.on_reset).pack(side=LEFT, padx=5)
        ttk.Button(input_frame, text="创建目录", bootstyle="succese", width=10, command=self.on_create_dir).pack(side=LEFT, padx=5)

        # 2. 选项复选框行
        check_frame = ttk.Frame(dir_group)
        check_frame.pack(fill=X, pady=(0, 10))
        
        options = [
            ("番号", self.is_av_var),
            ("4K", self.is_4k_var),
            ("破解", self.is_crack_var),
            ("LADA", self.is_lada_var),
            ("增强", self.is_enhance_var),
            ("流出", self.is_leaked_var),
            ("中字", self.is_cn_var),
        ]
        
        for i, (text, var) in enumerate(options):
            chk = ttk.Checkbutton(check_frame, text=text, variable=var, bootstyle="info-round-toggle")
            # chk.pack(side=RIGHT, padx=10)
            chk.grid(row=0, column=i, padx=10, sticky="w")

        # 3. 保存目录行
        save_frame = ttk.Frame(dir_group)
        save_frame.pack(fill=X)
        
        ttk.Label(save_frame, text="保存目录:", width=8).pack(side=LEFT)
        self.dir_entry = ttk.Entry(save_frame, textvariable=self.dir_var, state="readonly", bootstyle="secodnary")
        self.dir_entry.pack(side=LEFT, fill=X, expand=True, padx=5)
        
        ttk.Button(save_frame, text="浏览...", command=self.on_browse,bootstyle="outline", width=10).pack(side=LEFT, padx=5)
        ttk.Button(save_frame, text="打开目录", bootstyle="primary", command=self.on_open_dir, width=10).pack(side=LEFT, padx=5)

        # ------------------ 中部分：字幕查询下载 ------------------
        search_group = ttk.LabelFrame(main_container, text=" 字幕查询下载 ", padding=15)
        search_group.pack(fill=BOTH, expand=True)

        # 控制栏
        control_frame = ttk.Frame(search_group)
        control_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(control_frame, text="批量下载数量:").pack(side=LEFT, padx=5)
        spin = ttk.Spinbox(control_frame, from_=1, to=10, textvariable=self.batch_count_var, width=5, bootstyle="info")
        spin.pack(side=LEFT, padx=5)

        ttk.Button(control_frame, text="查询字幕", bootstyle='warning', command=self.on_search, width=10).pack(side=RIGHT, padx=5)
        ttk.Button(control_frame, text="批量下载", bootstyle="successs", command=self.on_batch_download, width=10).pack(side=RIGHT, padx=5)
        ttk.Button(control_frame, text="下载选中", bootstyle="primary-outline", command=self.on_download_selected, width=10).pack(side=RIGHT, padx=5)
        

        # 列表视图 - 恢复 4 列
        self.tree = ttk.Treeview(search_group, bootstyle="info", columns=("name", "lang", "time", "url"), show="headings")
    
        self.tree.heading("name", text="字幕名称")
        self.tree.heading("lang", text="语言")
        self.tree.heading("time", text="时长")
        self.tree.heading("url", text="下载链接")
        
        self.tree.column("name", width=300)
        self.tree.column("lang", width=50, anchor=CENTER)
        self.tree.column("time", width=50, anchor=CENTER)
        self.tree.column("url", width=300)

        vsb = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        # 添加水平滚动条，防止下载链接太长看不全
        hsb = ttk.Scrollbar(self.tree, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.pack(side=TOP, fill=BOTH, expand=True)
        vsb.pack(side=RIGHT, fill=Y)
        hsb.pack(side=BOTTOM, fill=X)

        # ------------------ 底部：状态栏 ------------------
        status_bar_frame = ttk.Frame(self, relief=RIDGE, padding=(5, 2))
        status_bar_frame.pack(side=BOTTOM, fill=X)
        
        # ttk.Label(status_bar_frame, textvariable=self.status_left_var, bootstyle="inverse-primary").pack(side=LEFT, padx=5)
        ttk.Label(status_bar_frame, textvariable=self.status_left_var, bootstyle="primary").pack(side=LEFT, padx=5)
        self.top_lbl = ttk.Label(status_bar_frame, textvariable=self.status_right_var, bootstyle="inverse-primary", cursor="hand2")
        self.top_lbl.pack(side=RIGHT, padx=5)
        self.top_lbl.bind("<Double-Button-1>", self.on_top_window)

        self.theme_lbl = ttk.Label(status_bar_frame, text="双击更改主题", bootstyle="inverse-warning", cursor="hand2")
        self.theme_lbl.pack(side=RIGHT, padx=5)
        self.theme_lbl.bind("<Double-Button-1>", self.on_change_theme)

    def _setup_listview(self):
        pass

    # ================= 业务逻辑部分 =================

    def _match_av(self, text):
        text = re.sub(r'[\\/:*?"<>|]', '', text)
        youma_pattern = re.compile(r'((?:\d{3})?[a-z]{2,5})[-_\s]?([\d]{2,5})(.*)$', re.IGNORECASE)
        fc_pattern = re.compile(r'(FC[2]?[-_\s]?(?:PPV)?)[-_\s]?(\d{7})(.*)$', re.IGNORECASE)
        p_lst = [fc_pattern, youma_pattern]
        match = None
        for pattern in p_lst:
            match = pattern.search(text)
            if match:
                sn = f"{match.group(1)}-{match.group(2)}"
                return sn.strip().upper(), f"{match.group(3)}".strip()
        if not match:
            return None, text.strip()

    def _format_duration(self, duration_ms):
        total_seconds = int(duration_ms) // 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def on_change_theme(self, event):
        stycle = ttk.Style()
        if self.theme_var == "litera":
            stycle.theme_use("superhero")
            self.theme_var = "superhero"
        else:
            stycle.theme_use("litera")
            self.theme_var = "litera"


    def on_create_dir(self):
        save_dir = self.dir_var.get()
        if not os.path.exists(save_dir):
            if messagebox.askyesno("目录不存在", "默认保存目录不存在，是否选择新目录？"):
                self.on_browse()
                save_dir = self.dir_var.get()
            else:
                return

        new_folder = self.name_var.get()
        sn, name_part = self._match_av(new_folder)
        
        if not self.is_av_var.get() or not sn:
            new_folder = re.sub(r'[\\/:*?"<>|]', '', new_folder)
        else:
            extend = ''
            if self.is_4k_var.get(): extend += '4K'
            if self.is_lada_var.get(): extend += 'La'
            elif self.is_crack_var.get(): extend += 'U'
            if self.is_leaked_var.get(): extend += 'L'
            if self.is_enhance_var.get(): extend += 'E'
            if self.is_cn_var.get(): extend += 'C'
            new_folder = f"{sn}-{extend} {name_part}" if name_part else f"{sn}-{extend}"

        if new_folder:
            try:
                name_folder_path = os.path.join(save_dir, new_folder)
                os.makedirs(name_folder_path, exist_ok=True)
                self.dir_var.set(name_folder_path)
                self.status_left_var.set(f"已创建新文件夹：{new_folder}")
            except Exception as e:
                messagebox.showerror("错误", f"创建文件夹失败：{e}")
                self.status_left_var.set(f"创建文件夹失败：{e}")

    def on_reset(self, event=None):
        self.name_var.set("")
        current_dir = self.dir_var.get()
        parent_dir = os.path.dirname(current_dir)
        self.dir_var.set(parent_dir)
        # 清空tree中项目：
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.status_left_var.set("准备就绪")

    def on_top_window(self, event=None):
        self.topmost_flag = not self.topmost_flag
        self.attributes('-topmost', self.topmost_flag)
        state = "双击取消置顶" if self.topmost_flag else "双击置顶窗口"
        self.status_right_var.set(f"{state}")

    def on_open_dir(self):
        dir_path = self.dir_var.get()
        if not os.path.exists(dir_path):
            messagebox.showwarning("警告", "目录不存在！")
            return

        if HAS_WIN32COM:
            try:
                shell = win32com.client.Dispatch("Shell.Application")
                windows = shell.Windows()
                explorer_window = None
                for i in range(windows.Count):
                    window = windows.Item(i)
                    if "explorer.exe" in window.FullName.lower():
                        explorer_window = window
                        break
                
                if explorer_window:
                    explorer_window.Navigate(dir_path)
                else:
                    os.startfile(dir_path)
                
                self.status_left_var.set(f"已打开：{dir_path}")
                self.on_reset()
            except Exception as e:
                messagebox.showerror("错误", f"无法打开目录：{str(e)}")
        else:
            os.startfile(dir_path)

    def on_browse(self):
        dialog = filedialog.askdirectory(title="选择保存文件夹")
        if dialog:
            self.dir_var.set(dialog)

    def on_search(self, event=None):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showinfo("提示", "请输入要查询的字幕名称！")
            return
        
        # 记录查询内容，用于显示在第一列
        self.search_content = name
                
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.search_results_data = []

        if self.is_av_var.get():
            sn, _ = self._match_av(name)
            if sn:
                name = sn

        self.status_left_var.set(f"正在查询 '{name}'...")
        threading.Thread(target=self._search_thread, args=(name,), daemon=True).start()

        try:
            search_in_everything = f'Everything.exe -s "{name}"'
            subprocess.run(search_in_everything, shell=True)
        except:
            pass

    def _search_thread(self, name):
        api_url = f"http://api-shoulei-ssl.xunlei.com/oracle/subtitle?name={quote(name)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        try:
            response = requests.get(api_url, headers=headers, timeout=8)
            response.raise_for_status()
            data = response.json()
            
            if data.get('code') == 0 and 'data' in data:
                subtitles = data['data']
                self.after(0, self._update_list_ui, subtitles)
                self.after(0, lambda: self.status_left_var.set(f"查询成功，找到 {len(subtitles)} 条结果。    查询内容：{name}"))
            else:
                self.after(0, lambda: self.status_left_var.set(f"查询失败: {data.get('result')}。    查询内容：{name}"))
        except Exception as e:
            self.after(0, lambda: self.status_left_var.set(f"网络错误: {str(e)}"))

    def _update_list_ui(self, subtitles):
        self.search_results_data = subtitles
        for item in subtitles:
            languages = "&".join(item.get('languages', []))
            duration = self._format_duration(item.get('duration', 0))
            # 插入数据顺序：name, lang, time, url
            self.tree.insert("", END, values=(
                item.get('name', ''),   # 0: 字幕名称
                languages,              # 1: 语言
                duration,               # 2: 时长
                item.get('url', '')     # 3: 下载链接
            ))

    def _get_selected_items(self):
        """获取选中的 Treeview 项对应的数据"""
        selected_items = []
        selected_ids = self.tree.selection()
        if not selected_ids:
            return []
        
        for item_id in selected_ids:
            values = self.tree.item(item_id)['values']
            if values:
                # values 索引修正为 4 列结构
                # 0: name, 1: lang, 2: time, 3: url
                selected_items.append({
                    'name': values[0],
                    'languages': values[1].split('&') if values[1] else [],
                    'url': values[-1]
                })
        return selected_items

    def on_download_selected(self):
        save_dir = self.dir_var.get()
        if not save_dir or not os.path.exists(save_dir):
            messagebox.showinfo("提示", "请先选择/确认有效的保存目录！")
            return
        
        items = self._get_selected_items()
        if not items:
            messagebox.showinfo("提示", "请至少选择一个字幕！")
            return

        self.status_left_var.set(f"开始下载 {len(items)} 个文件...")
        threading.Thread(target=self._download_thread, args=(items, save_dir), daemon=True).start()

    def on_batch_download(self):
        save_dir = self.dir_var.get()
        if not save_dir or not os.path.exists(save_dir):
            messagebox.showinfo("提示", "请先选择/确认有效的保存目录！")
            return
        
        if not self.search_results_data:
            messagebox.showinfo("提示", "请先查询字幕列表！")
            return

        count = self.batch_count_var.get()
        
        priority_map = {'简体': 0, '繁体': 1, '英语': 3}
        sorted_results = sorted(self.search_results_data, key=lambda x: min([priority_map.get(l, 2) for l in x.get('languages', [])]))
        
        items = sorted_results[:count]
        self.status_left_var.set(f"开始批量下载 {len(items)} 个文件...")
        threading.Thread(target=self._download_thread, args=(items, save_dir), daemon=True).start()

    def _download_thread(self, items, save_dir):
        success = 0
        fail = 0
        for i, item in enumerate(items):
            url = item.get('url')
            filename = item.get('name', f"subtitle_{i}.srt").replace("/", "_").replace("\\", "_")
            
            if not filename.endswith('.srt') and not os.path.splitext(filename)[1]:
                filename += ".srt"
            
            filepath = os.path.join(save_dir, filename)
            if os.path.exists(filepath):
                base, ext = os.path.splitext(filepath)
                counter = 1
                while os.path.exists(f"{base}_{counter}{ext}"):
                    counter += 1
                filepath = f"{base}_{counter}{ext}"
                filename = os.path.basename(filepath)

            self.after(0, lambda f=filename: self.status_left_var.set(f"正在下载: {f}"))
            
            try:
                r = requests.get(url, stream=True, timeout=15)
                r.raise_for_status()
                with open(filepath, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                success += 1
            except:
                fail += 1
        
        msg = f"下载完成！成功 {success} 个，失败 {fail} 个。"
        self.after(0, lambda: self.status_left_var.set(msg))

if __name__ == '__main__':
    app = SubtitleDownloaderFrame()
    app.mainloop()
