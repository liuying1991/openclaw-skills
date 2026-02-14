---
name: cherry-studio
description: Cherry Studio 操控技能。Cherry Studio 是一款跨平台 AI 桌面应用，集成 300+ 大模型。支持小程序功能，可快速访问 qwenlm (通义千问) 等 AI 服务。用于替代 OpenClaw 的网络搜索，更快更高效。
allowed-tools: Bash
---

# Cherry Studio 操控技能

**一站式 AI 助手平台，集成 300+ 大模型**

---

## 🎯 核心功能

| 功能 | 说明 |
|------|------|
| **多模型支持** | OpenAI、Claude、Gemini、通义千问等 300+ 模型 |
| **小程序** | 快速访问 AI 网页版，如 qwenlm (chat.qwen.ai) |
| **知识库** | 导入文档构建个性化 AI 助手 |
| **免费使用** | 内置免费模型，无需 API Key |

---

## 📥 安装信息

**桌面快捷方式**: `C:\Users\Administrator.WIN-15VSDGCVDE6\Desktop\Cherry Studio.lnk`

**数据目录**: `C:\Users\Administrator.WIN-15VSDGCVDE6\AppData\Roaming\CherryStudio`

---

## 🚀 启动 Cherry Studio

### 方法1：桌面快捷方式

```powershell
# 启动 Cherry Studio
Start-Process "C:\Users\Administrator.WIN-15VSDGCVDE6\Desktop\Cherry Studio.lnk"
```

### 方法2：直接运行

```powershell
# 查找并运行 Cherry Studio.exe
$shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut("C:\Users\Administrator.WIN-15VSDGCVDE6\Desktop\Cherry Studio.lnk")
Start-Process $shortcut.TargetPath
```

---

## 🖥️ 界面布局

```
┌─────────────────────────────────────────────────────────┐
│                    顶部菜单栏                            │
├──────────┬──────────────────────────────────────────────┤
│          │                                              │
│  左侧    │              主内容区                         │
│  边栏    │                                              │
│          │    ┌────────────────────────────────┐       │
│  小程序   │    │                                │       │
│  列表    │    │      AI 对话区域               │       │
│          │    │      (输入框 + 输出区)          │       │
│  qwenlm  │    │                                │       │
│  豆包    │    └────────────────────────────────┘       │
│  Kimi    │                                              │
│  ...     │                                              │
│          │                                              │
├──────────┴──────────────────────────────────────────────┤
│                    状态栏                                │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 qwenlm 小程序操控

### qwenlm 是什么？

**qwenlm 小程序 = 通义千问网页版 (chat.qwen.ai)**

这是阿里云的免费 AI 服务，可以快速回答问题、搜索知识。

### 操控流程

```
1. 启动 Cherry Studio
2. 点击左侧边栏的 qwenlm 小程序
3. 等待页面加载
4. 在输入框输入问题
5. 等待 AI 回答
6. 复制回答内容
7. 返回 OpenClaw 报告结果
```

### 键盘操控命令

```powershell
# 1. 启动 Cherry Studio
Start-Process "C:\Users\Administrator.WIN-15VSDGCVDE6\Desktop\Cherry Studio.lnk"
Start-Sleep -Seconds 5

# 2. 激活窗口
Add-Type -AssemblyName System.Windows.Forms
Add-Type @"
  using System;
  using System.Runtime.InteropServices;
  public class Win32 {
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
  }
"@

# 获取 Cherry Studio 窗口
$process = Get-Process | Where-Object { $_.ProcessName -like "*Cherry*" -or $_.MainWindowTitle -like "*Cherry*" } | Select-Object -First 1
if ($process) {
    [Win32]::SetForegroundWindow($process.MainWindowHandle)
}

# 3. 点击 qwenlm 小程序 (假设在左侧边栏)
# 使用 Tab 导航到小程序列表
[System.Windows.Forms.SendKeys]::SendWait("{TAB}")
Start-Sleep -Milliseconds 200
[System.Windows.Forms.SendKeys]::SendWait("{TAB}")
Start-Sleep -Milliseconds 200

# 4. 输入问题
[System.Windows.Forms.SendKeys]::SendWait("搜索鸡蛋的营养成分和健康好处")
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")

# 5. 等待回答
Start-Sleep -Seconds 10

# 6. 复制回答 (Ctrl+A 全选 + Ctrl+C 复制)
[System.Windows.Forms.SendKeys]::SendWait("^(a)")
Start-Sleep -Milliseconds 200
[System.Windows.Forms.SendKeys]::SendWait("^(c)")

# 7. 获取剪贴板内容
$result = Get-Clipboard
```

---

## 📋 使用场景

### 场景1：快速搜索知识

**用户请求**: "搜索鸡蛋的营养信息"

**执行步骤**:
1. 启动 Cherry Studio
2. 打开 qwenlm 小程序
3. 输入问题
4. 获取回答
5. 返回结果给用户

**优势**: 比 OpenClaw 自己搜索更快，直接利用 AI 的知识库

### 场景2：文献资料查询

**用户请求**: "查找关于 AI 发展的资料"

**执行步骤**:
1. 打开 qwenlm
2. 输入查询
3. 获取总结
4. 返回给用户

### 场景3：多模型对比

**用户请求**: "对比不同 AI 的回答"

**执行步骤**:
1. 在 Cherry Studio 中打开多个小程序
2. 分别提问
3. 对比结果
4. 返回对比报告

---

## ⚡ 效率对比

| 方式 | 耗时 | 说明 |
|------|------|------|
| OpenClaw 自己搜索 | 30+ 秒 | 搜索 + 获取网页 + 分析 |
| Cherry Studio qwenlm | 10 秒 | 直接提问 + 获取回答 |

**结论**: 使用 Cherry Studio 更快！

---

## 🔍 小程序列表

Cherry Studio 内置多个小程序：

| 小程序 | 网址 | 用途 |
|--------|------|------|
| **qwenlm** | chat.qwen.ai | 通义千问，免费 AI |
| 豆包 | doubao.com | 字节跳动 AI |
| Kimi | kimi.moonshot.cn | 月之暗面 AI |
| DeepSeek | chat.deepseek.com | 深度求索 AI |

---

## 💡 使用技巧

### 1. 快速切换小程序

```powershell
# Tab 导航到小程序列表
[System.Windows.Forms.SendKeys]::SendWait("{TAB}")

# 上下箭头选择
[System.Windows.Forms.SendKeys]::SendWait("{DOWN}")
[System.Windows.Forms.SendKeys]::SendWait("{UP}")

# Enter 确认
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
```

### 2. 快速输入

```powershell
# 直接输入问题
[System.Windows.Forms.SendKeys]::SendWait("你的问题")
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
```

### 3. 快速复制

```powershell
# Ctrl+A 全选
[System.Windows.Forms.SendKeys]::SendWait("^(a)")

# Ctrl+C 复制
[System.Windows.Forms.SendKeys]::SendWait("^(c)")

# 获取剪贴板
$result = Get-Clipboard
```

---

## ⚠️ 注意事项

1. **等待加载** - 小程序需要时间加载，要等待
2. **窗口激活** - 键盘输入前确保窗口已激活
3. **延迟操作** - 操作之间要有延迟
4. **错误处理** - 如果失败，重试或切换方案

---

## 📊 与 OpenClaw 整合

### 整合流程

```
用户请求
    │
    ├─ 判断任务类型
    │   ├─ 需要搜索知识？ → 使用 Cherry Studio qwenlm
    │   └─ 需要获取网页？ → 使用 Playwright
    │
    ├─ 执行 Cherry Studio 操控
    │   ├─ 启动 Cherry Studio
    │   ├─ 打开 qwenlm
    │   ├─ 输入问题
    │   └─ 获取回答
    │
    └─ 返回结果给用户
```

### 优势

| 优势 | 说明 |
|------|------|
| **更快** | 直接获取 AI 回答，无需搜索网页 |
| **更准** | AI 理解问题，给出精准回答 |
| **更省** | 免费 AI 服务，无需 API 费用 |

---

## 🔗 相关链接

- 官网: https://www.cherry-ai.com
- 文档: https://docs.cherry-ai.com
- GitHub: https://github.com/kangfenmao/cherry-studio

---

**Cherry Studio 让 OpenClaw 更快更高效！**
