---
name: trae-cn-ide
description: Trae CN AI IDE 完整使用指南。字节跳动推出的免费 AI 原生 IDE，支持 SOLO 模式、SOLO Coder、Plan 模式、一键部署、前后端联调。最新版本 v3.3.x。
allowed-tools: Bash
---

# Trae CN AI IDE 完整使用指南

**字节跳动推出的免费 AI 原生 IDE，专为中文开发者设计**

---

## 🎯 核心特点

| 特点 | 说明 |
|------|------|
| **SOLO 模式** | AI 自主开发，一键部署 |
| **SOLO Coder** | 内置智能体，支持复杂项目 |
| **Plan 模式** | 清晰规划，精准执行 |
| **多任务并行** | 告别单线程限制 |
| **一键部署** | 自动构建、托管、联调 |
| **免费使用** | 全部功能完全免费 |

---

## 🚀 SOLO 模式 - 核心功能

### SOLO 模式是什么？

SOLO 模式是 Trae 针对独立开发者做的深度减负方案：
- AI 自动分析和梳理需求
- AI 灵活调度编辑器、浏览器、终端、文档等工具
- 通过 SOLO Builder 智能体快速搭建前端应用
- 实时跟随 AI 操作，自动切换工具面板

### SOLO Coder 智能体

**内置智能体，支持复杂编程项目**

| 功能 | 说明 |
|------|------|
| 需求分析 | 自动分析需求，生成可编辑的产品需求文档 |
| 任务拆解 | 智能拆解任务并标记完成情况 |
| 代码生成 | 多轮对话生成项目级代码 |
| 实时预览 | 自动打开预览，实时查看效果 |

### Plan 模式

**从清晰的规划开始，让任务精准推进执行**

**快捷键**: `Alt + P` (Windows) / `Option + P` (macOS)

**功能**:
- AI 生成执行计划
- 可编辑调整计划
- 按计划逐步执行
- 任务完成自动折叠

### 多任务并行

- 支持同时进行多个任务
- 已完成任务自动折叠并生成摘要
- 提高工作效率

---

## 📥 安装配置

### 下载地址

- 中国版: https://trae.com.cn
- 海外版: https://www.trae.ai

### 安装步骤

1. **下载安装包** - 访问官网选择对应系统版本
2. **初始配置**
   - 选择主题（暗色/亮色/深蓝）
   - 选择语言（默认简体中文）
   - 可选：导入 VS Code/Cursor 配置
3. **安装命令行工具** - 点击「安装 trae 命令」
4. **登录认证** - 使用手机号或掘金账号登录

### 命令行启动

```bash
# 打开项目
trae /path/to/project

# 或在项目目录下
cd /path/to/project
trae .
```

---

## 🖥️ 界面布局

### IDE 模式

```
┌─────────────────────────────────────────────────────────┐
│                    顶部菜单栏                            │
├──────────┬──────────────┬─────────────────┬─────────────┤
│  侧边栏   │    文件区    │    代码编辑区    │  AI 对话区  │
│ Explorer │   文件树     │    代码内容     │   Chat/     │
│ Search   │              │                 │   Builder   │
│ Git      │              │                 │             │
│ WebView  │              │                 │             │
│ Debug    │              │                 │             │
│ Extension│              │                 │             │
├──────────┴──────────────┴─────────────────┴─────────────┤
│                    底部终端/状态栏                        │
└─────────────────────────────────────────────────────────┘
```

### SOLO 模式

```
┌─────────────────────────────────────────────────────────┐
│                    顶部工具栏                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│                    AI 对话区域                          │
│              (需求输入、任务列表、代码变更)               │
│                                                         │
├──────────────────────┬──────────────────────────────────┤
│     代码编辑区        │         预览/浏览器区            │
│                      │                                  │
│                      │                                  │
├──────────────────────┴──────────────────────────────────┤
│                    终端/日志区                           │
└─────────────────────────────────────────────────────────┘
```

---

## ⌨️ 快捷键速查

### 基础操作

| 操作 | Windows | macOS |
|------|---------|-------|
| 新建文件 | Ctrl+N | Command+N |
| 打开命令面板 | Ctrl+Shift+P | Command+Shift+P |
| 全局搜索 | Ctrl+Shift+F | Command+Shift+F |
| 注释代码 | Ctrl+/ | Command+/ |

### AI 功能

| 操作 | Windows | macOS |
|------|---------|-------|
| AI 对话框 | Ctrl+U | Command+U |
| Plan 模式 | Alt+P | Option+P |
| 代码补全 | Ctrl+Space | Command+Space |
| Pro 补全 | Ctrl+Shift+Enter | Command+Shift+Enter |
| Git Commit | Ctrl+G | Command+G |
| 报告问题 | Ctrl+K Ctrl+R | Command+K Command+R |

### AI 命令

```
/explain    - 代码解释
/fix        - 修复错误
/test       - 生成测试
/doc        - 生成注释
```

---

## 🔧 核心 AI 功能

### 1. Builder 模式

**适合场景**: 从零搭建项目

**使用方法**:
1. 打开 Builder 模式
2. 用中文描述需求
3. AI 自动分析、规划、执行
4. 实时预览效果

**示例**:
```
用户输入: "做一个聊天应用，支持消息发送和接收"
AI 输出: 
  1. 分析需求 → 生成产品需求文档
  2. 创建项目结构
  3. 生成前端代码
  4. 生成后端代码
  5. 自动预览
```

### 2. Chat 模式

**适合场景**: 调试排错、代码理解、问题咨询

**使用方法**:
1. 打开 Chat 模式
2. 输入问题，可用 `#` 关联文件
3. AI 给出解决方案，支持多轮追问

**上下文引用**:
- `#文件名` - 引用文件
- `#文件夹` - 引用文件夹
- `#Web` - 联网搜索
- `#Doc` - 引用文档

### 3. 智能代码补全 (Cue)

**两种模式**:

| 模式 | 触发方式 | 说明 |
|------|----------|------|
| 基础补全 | 换行/添加注释后自动触发 | 按 Tab 采纳 |
| Pro 补全 | Ctrl+Shift+Enter | 跨文件感知上下文 |

**功能**:
- 多行修改
- 修改点预测
- 修改点跳转
- 智能导入
- 智能重命名

---

## 🚀 一键部署

### 部署流程

```
代码推送 → 自动构建 → 自动托管 → 生成访问地址
```

**部署地址格式**: `https://your-app.trae.dev`

### 前后端联调

**配置文件**: `trae.yaml`

```yaml
version: "1.0"
services:
  api:
    port: 8080
    path: /api
    health_check: /health
```

**前端调用**:
```javascript
// 直接使用相对路径，无需配置跨域
fetch("/api/messages")
```

### 环境变量

**方式1**: Web 控制台手动填写

**方式2**: `.env.trae` 文件
```
API_BASE_URL=https://api.example.com
NODE_ENV=development
```

---

## 📋 技能系统

### 创建技能

1. 打开设置 → 技能
2. 点击「创建技能」
3. 编写技能描述和提示词
4. 保存并启用

### 使用技能

- 全局技能：所有项目可用
- 项目技能：仅当前项目可用
- 在对话中通过 `@技能名` 调用

---

## 🔒 沙箱运行

### 三种运行模式

| 模式 | 说明 |
|------|------|
| 沙箱运行 | 默认启用，命令在安全沙箱中运行 |
| 手动运行 | 所有命令需手动确认 |
| 自动运行 | 所有命令自动在沙箱外执行 |

### 白名单配置

在设置中配置白名单命令，无需经过沙箱直接运行。

---

## 🔄 代码变更工具 (DiffView)

### 功能

- 集中展示代码变更历史
- 支持对比查看
- 支持版本回退
- 支持批量接受/拒绝

### 操作

- `Accept` - 接受变更
- `Reject` - 拒绝变更
- 红色背景 = 删除的代码
- 绿色背景 = 新增的代码

---

## 📊 上下文管理

### 上下文使用率

- 实时展示上下文使用情况
- 支持上下文压缩
- 自动管理上下文窗口

### 上下文类型

| 类型 | 说明 |
|------|------|
| 文件 | 单个文件内容 |
| 文件夹 | 整个文件夹内容 |
| 代码片段 | 选中的代码 |
| 终端日志 | 终端输出内容 |
| 网页 | #Web 联网搜索 |
| 文档 | #Doc 文档内容 |

---

## 🖥️ 电脑操控 Trae CN

### 如何操控 Trae CN

**使用 PowerShell 键盘控制**:

```powershell
# 1. 启动 Trae
Start-Process trae

# 2. 等待启动
Start-Sleep -Seconds 3

# 3. 发送快捷键
Add-Type -AssemblyName System.Windows.Forms

# 打开 AI 对话框
[System.Windows.Forms.SendKeys]::SendWait("^(u)")  # Ctrl+U

# 输入需求
[System.Windows.Forms.SendKeys]::SendWait("创建一个 React 项目")

# 发送
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
```

### 操控流程

```
1. 启动 Trae → Start-Process trae
2. 打开项目 → trae /path/to/project
3. 唤起 AI → Ctrl+U
4. 输入需求 → SendKeys
5. 等待执行 → Start-Sleep
6. 验证结果 → 检查文件/预览
```

### 常用操控场景

**场景1：创建新项目**
```powershell
# 启动 Trae
Start-Process trae
Start-Sleep -Seconds 5

# 唤起 AI 对话
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("^(u)")
Start-Sleep -Milliseconds 500

# 输入需求
[System.Windows.Forms.SendKeys]::SendWait("创建一个 Vue3 项目，包含登录页面")
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
```

**场景2：修改代码**
```powershell
# 唤起 AI 对话
[System.Windows.Forms.SendKeys]::SendWait("^(u)")

# 输入修改需求
[System.Windows.Forms.SendKeys]::SendWait("修改 App.vue，添加导航栏组件")
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")

# 等待生成
Start-Sleep -Seconds 10

# 接受变更 (假设 Tab 是接受)
[System.Windows.Forms.SendKeys]::SendWait("{TAB}")
```

**场景3：运行项目**
```powershell
# 唤起 AI 对话
[System.Windows.Forms.SendKeys]::SendWait("^(u)")

# 请求运行
[System.Windows.Forms.SendKeys]::SendWait("运行这个项目")
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
```

---

## 💡 使用技巧

### 1. 高效使用 SOLO 模式

```
❌ 模糊描述: "做一个网站"
✅ 清晰描述: "做一个个人博客网站，包含文章列表、详情页、评论功能，使用 React + Node.js"
```

### 2. 使用 Plan 模式

```
1. 按 Alt+P 开启 Plan 模式
2. 输入需求
3. AI 生成执行计划
4. 编辑调整计划
5. 确认执行
```

### 3. 多任务并行

```
1. 创建多个任务
2. AI 并行处理
3. 查看任务列表
4. 完成的任务自动折叠
```

### 4. 上下文压缩

```
当上下文使用率过高时：
1. AI 自动压缩历史对话
2. 保留关键信息
3. 继续对话
```

---

## ⚠️ 常见问题

| 问题 | 解决方案 |
|------|----------|
| AI 功能无法使用 | 检查是否登录，网络是否正常 |
| SOLO 模式等待中 | 需要加入等待名单，按顺序开放 |
| 部署失败 | 检查项目结构，确保有正确的入口文件 |
| 快捷键冲突 | 进入快捷键设置修改 |
| 命令执行失败 | 检查沙箱设置，添加白名单 |

---

## 📊 版本信息

| 版本 | 发布日期 | 主要功能 |
|------|----------|----------|
| v3.3.x | 2026-01 | 技能系统、沙箱优化 |
| v3.0.0 | 2025-11 | SOLO 模式免费开放 |
| v2.0.0 | 2025-07 | 全新视觉设计、SOLO 模式 |

---

## 🔗 相关链接

- 官网: https://trae.com.cn
- 文档: https://docs.trae.ai
- 更新日志: https://m.w3cschool.cn/traedocs/trae-changelog.html

---

**Trae CN 是中文开发者最佳的 AI IDE 选择！**
