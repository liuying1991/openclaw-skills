---
name: windows-gui-control
description: Windows 桌面 GUI 控制技能。使用 PyAutoGUI 控制鼠标和键盘，模拟人类操作电脑软件。支持截图、点击、输入、滚动等操作。适用于 Windows 10/11 系统。
allowed-tools: Bash
---

# Windows GUI 控制技能

**使用 PyAutoGUI 模拟人类操作 Windows 桌面**

---

## 核心能力

| 功能 | 命令 | 说明 |
|------|------|------|
| 截图 | `screenshot` | 获取当前屏幕内容 |
| 鼠标位置 | `position` | 获取当前鼠标坐标 |
| 移动鼠标 | `move <x> <y>` | 移动到指定坐标 |
| 点击 | `click <x> <y> [button] [clicks]` | 鼠标点击 |
| 输入文字 | `type <text>` | 通过剪贴板输入中文 |
| 按键 | `key <key>` | 按键或组合键 |
| 滚动 | `scroll <direction> [amount]` | 滚动屏幕 |

---

## 使用方法

### Python脚本路径
```
C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py
```

### 命令示例

```powershell
# 截图
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" screenshot

# 获取鼠标位置
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" position

# 移动鼠标到坐标 (500, 400)
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" move 500 400

# 左键点击
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" click 500 400

# 双击
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" click 500 400 left 2

# 输入中文
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" type "你好世界"

# 按Enter键
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" key enter

# 按Ctrl+C
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" key ctrl+c

# 向下滚动3次
python "C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\windows-gui-control\scripts\gui_control.py" scroll down 3
```

---

## 操作流程模式

```
┌─────────────┐
│  1. 截图    │ → 查看当前屏幕状态
└──────┬──────┘
       ↓
┌─────────────┐
│  2. 分析    │ → 识别UI元素位置
└──────┬──────┘
       ↓
┌─────────────┐
│  3. 操作    │ → 点击/输入/滚动
└──────┬──────┘
       ↓
┌─────────────┐
│  4. 验证    │ → 再次截图确认结果
└──────┬──────┘
       ↓
   重复或完成
```

---

## Cherry Studio 操控示例

### 完整流程

```
1. 截图查看当前屏幕
2. 启动 Cherry Studio（通过 exec 或 process 工具）
3. 等待5秒让应用加载
4. 再次截图查看界面
5. 点击 qwenlm 小程序图标
6. 输入问题
7. 等待回答
8. 截图获取结果
```

### 示例命令序列

```powershell
# 1. 截图
python gui_control.py screenshot

# 2. 启动 Cherry Studio
start "" "C:\Users\Administrator.WIN-15VSDGCVDE6\Desktop\Cherry Studio.lnk"

# 3. 等待5秒
timeout /t 5

# 4. 再次截图
python gui_control.py screenshot

# 5. 点击小程序图标 (坐标需要根据截图确定)
python gui_control.py click 100 300

# 6. 输入问题
python gui_control.py type "请解释量子纠缠"

# 7. 发送
python gui_control.py key enter

# 8. 等待回答后截图
python gui_control.py screenshot
```

---

## 坐标系统

```
(0,0) ──────────────────────► X
  │
  │     ┌─────────────┐
  │     │             │
  │     │   屏幕      │
  │     │             │
  │     └─────────────┘
  │
  ▼
  Y
```

- 原点 (0,0) 在屏幕左上角
- X 向右增加
- Y 向下增加
- 使用截图确定具体坐标

---

## 安全设置

```python
import pyautogui

# 启用防故障功能（鼠标移到左上角停止）
pyautogui.FAILSAFE = True

# 设置操作间隔
pyautogui.PAUSE = 0.1
```

---

## 注意事项

1. **防故障**: 鼠标移到屏幕左上角可紧急停止
2. **延迟**: 操作之间要有适当延迟
3. **验证**: 每次操作后截图验证结果
4. **中文输入**: 使用剪贴板方式输入中文

---

## 返回值格式

所有命令返回 JSON 格式：

```json
{
  "status": "success",
  "action": "screenshot",
  "width": 1920,
  "height": 1080,
  "save_path": "..."
}
```

---

**Windows GUI 控制技能让 OpenClaw 真正像人一样操作电脑！**
