---
name: software-operations
description: Knowledge base for operating third-party software. Contains operation guides for common applications like Word, Excel, Chrome, VS Code, etc.
allowed-tools: Bash
---

# Software Operations Knowledge Base

Knowledge base for operating third-party software on Windows.

## Supported Applications

### Office Suite
| 软件 | 可执行文件 | 主要功能 | 操作方式 |
|------|------------|----------|----------|
| Microsoft Word | winword.exe | 文档编辑 | 键盘快捷键、菜单操作 |
| Microsoft Excel | excel.exe | 表格处理 | 公式、数据操作 |
| Microsoft PowerPoint | powerpnt.exe | 演示文稿 | 幻灯片编辑 |
| Notepad | notepad.exe | 文本编辑 | 简单文本操作 |
| WordPad | wordpad.exe | 富文本编辑 | 格式化文本 |

### Browsers
| 软件 | 可执行文件 | 主要功能 | 操作方式 |
|------|------------|----------|----------|
| Google Chrome | chrome.exe | 网页浏览 | URL导航、标签管理 |
| Microsoft Edge | msedge.exe | 网页浏览 | URL导航、标签管理 |
| Firefox | firefox.exe | 网页浏览 | URL导航、标签管理 |

### Development Tools
| 软件 | 可执行文件 | 主要功能 | 操作方式 |
|------|------------|----------|----------|
| VS Code | code.exe | 代码编辑 | 文件操作、终端 |
| Notepad++ | notepad++.exe | 代码编辑 | 语法高亮 |
| Git Bash | git-bash.exe | 版本控制 | 命令行操作 |

### Media Players
| 软件 | 可执行文件 | 主要功能 | 操作方式 |
|------|------------|----------|----------|
| VLC | vlc.exe | 视频播放 | 播放控制 |
| Windows Media Player | wmplayer.exe | 媒体播放 | 播放控制 |

### Communication
| 软件 | 可执行文件 | 主要功能 | 操作方式 |
|------|------------|----------|----------|
| WeChat | WeChat.exe | 即时通讯 | 消息发送 |
| DingTalk | DingTalk.exe | 企业通讯 | 消息发送 |
| Feishu | Lark.exe | 企业协作 | 消息、文档 |

## Operation Guides

### Microsoft Word Operations

**打开文档**
```powershell
Start-Process winword.exe -ArgumentList "C:\path\to\document.docx"
```

**常用快捷键**
| 操作 | 快捷键 |
|------|--------|
| 保存 | Ctrl+S |
| 复制 | Ctrl+C |
| 粘贴 | Ctrl+V |
| 全选 | Ctrl+A |
| 查找 | Ctrl+F |
| 替换 | Ctrl+H |
| 加粗 | Ctrl+B |
| 斜体 | Ctrl+I |
| 下划线 | Ctrl+U |

### Google Chrome Operations

**打开网页**
```powershell
Start-Process chrome.exe -ArgumentList "https://www.example.com"
```

**常用快捷键**
| 操作 | 快捷键 |
|------|--------|
| 新标签页 | Ctrl+T |
| 关闭标签 | Ctrl+W |
| 刷新 | F5 |
| 地址栏 | Ctrl+L |
| 查找 | Ctrl+F |
| 开发者工具 | F12 |

### VS Code Operations

**打开项目**
```powershell
Start-Process code.exe -ArgumentList "C:\path\to\project"
```

**常用快捷键**
| 操作 | 快捷键 |
|------|--------|
| 命令面板 | Ctrl+Shift+P |
| 文件搜索 | Ctrl+P |
| 全局搜索 | Ctrl+Shift+F |
| 终端 | Ctrl+` |
| 保存 | Ctrl+S |
| 格式化 | Shift+Alt+F |

## Automation Examples

### Example 1: Create Word Document
```
User: "创建一个 Word 文档并写入内容"

Steps:
1. app-control: 打开 Word
2. keyboard-mouse-control: 等待窗口激活
3. keyboard-mouse-control: 输入内容
4. keyboard-mouse-control: Ctrl+S 保存
5. keyboard-mouse-control: 输入文件名
6. keyboard-mouse-control: Enter 确认
```

### Example 2: Browse Website
```
User: "用 Chrome 打开百度搜索 Python"

Steps:
1. app-control: 打开 Chrome
2. keyboard-mouse-control: Ctrl+L 聚焦地址栏
3. keyboard-mouse-control: 输入 baidu.com
4. keyboard-mouse-control: Enter 打开
5. keyboard-mouse-control: Tab 聚焦搜索框
6. keyboard-mouse-control: 输入 Python
7. keyboard-mouse-control: Enter 搜索
```

### Example 3: Edit Code in VS Code
```
User: "在 VS Code 中打开项目并运行"

Steps:
1. app-control: 打开 VS Code
2. keyboard-mouse-control: Ctrl+P 搜索文件
3. keyboard-mouse-control: 输入文件名
4. keyboard-mouse-control: Enter 打开
5. keyboard-mouse-control: Ctrl+` 打开终端
6. keyboard-mouse-control: 输入运行命令
```

## Software Detection

### Check if Software is Installed
```powershell
# Check by executable
Get-Command chrome.exe -ErrorAction SilentlyContinue

# Check by registry
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | 
    Where-Object { $_.DisplayName -like "*Chrome*" }
```

### Get Installed Software List
```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher |
    Where-Object { $_.DisplayName }
```

## Best Practices

1. **验证软件已安装** - 操作前检查软件是否存在
2. **使用快捷键** - 比鼠标点击更可靠
3. **添加延迟** - 等待窗口加载完成
4. **错误处理** - 处理窗口未响应情况
5. **保存工作** - 操作完成后保存

## Extending Knowledge Base

要添加新软件的操作知识：

1. 确定可执行文件名
2. 记录常用快捷键
3. 测试自动化操作
4. 添加到知识库
5. 创建 SKILL 文件
