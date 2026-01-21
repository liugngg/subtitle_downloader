# 字幕查找工具

## 1.主要功能

1. 通过迅雷影音接口查询字幕。

2. 支持命名文件夹并打开。

3. 查询字幕时，如果将 Everything.exe 加入的系统路径里，可以同步本地查询。

## 2. 打包命令

- 生成单文件格式（pyinstaller）
  `pyinstaller -i liug.ico -F -w subtitle_downloader.py --clean -n 字幕查询工具-liug`

- 生成单文件格式（Nuitka --onefile自动压缩）
  
  `python -m nuitka --mingw64 --onefile --lto=yes --show-progress --output-dir=dist --remove-output --include-package=wx --windows-console-mode=disable --windows-icon-from-ico=liug.ico subtitle_downloader.py`

- 生成单文件格式（Nuitka --使用upx 压缩）
  
  `python -m nuitka --mingw64 --onefile --onefile-no-compression --plugin-enable=upx --lto=yes --show-progress --output-dir=dist --remove-output --include-package=wx --windows-console-mode=disable --windows-icon-from-ico=liug.ico subtitle_downloader.py`

## 3. 作者

- [liugngg (GitHub地址)](https://github.com/liugngg)
