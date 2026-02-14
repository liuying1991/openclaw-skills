---
name: find-skills
description: 搜索和发现系统技能。当用户问"有什么技能"、"搜索技能"、"browser相关技能"时使用。执行步骤：1.exec列出技能目录 2.read读取SKILL.md 3.生成报告
---

# Find Skills - 技能搜索

## ⚠️ 执行方式 - 必须按此步骤

### 步骤 1：列出本地技能
使用 `exec` 工具执行：
```powershell
Get-ChildItem C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills -Directory | Select-Object Name
```

### 步骤 2：读取技能描述
使用 `read` 工具读取每个技能的 SKILL.md：
```
C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\技能名\SKILL.md
```

### 步骤 3：生成报告
使用 `write` 工具创建报告文件

---

## 本地技能搜索

### 搜索所有技能
```powershell
Get-ChildItem C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills -Directory | ForEach-Object { $_.Name }
```

### 搜索特定关键词
```powershell
Get-ChildItem C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills -Directory | Where-Object { $_.Name -like "*关键词*" }
```

---

## 本地技能目录
```
C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\
```

---

## 已安装的技能列表

| 技能名称 | 功能描述 |
|----------|----------|
| auto-service-manager | 自动化服务管理 |
| cherry-studio | 多模态图像/音频生成 |
| clawdbot-filesystem | 文件系统操作 |
| computer-use | 电脑交互控制 |
| core-skills-index | 核心技能索引 |
| error-recovery | 错误恢复 |
| find-skills | 技能搜索 |
| knowledge-organizer | 知识组织 |
| learning-memory | 学习记忆 |
| playwright-browser | 浏览器自动化 |
| proactive-agent | 主动代理 |
| software-operations | 软件操作 |
| task-prioritizer | 任务优先级 |
| trae-cn-ide | IDE 集成 |
| web-search | 网络搜索 |
| windows-gui-control | Windows GUI 控制 |

---

## 完整示例：搜索 browser 相关技能

**用户请求：** "搜索所有与 browser 相关的技能"

**执行步骤：**

1. **exec** 列出所有技能：
```powershell
Get-ChildItem C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills -Directory | Select-Object Name
```

2. **筛选** 包含 browser 的技能：
- playwright-browser

3. **read** 读取技能描述：
```
C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\playwright-browser\SKILL.md
```

4. **write** 生成报告：
```
C:\tmp\browser-skills.md
```

---

## 外部技能搜索

如果需要搜索外部可安装的技能，使用：
```bash
npx skills find [query]
```

浏览更多技能：https://skills.sh/

---

## ❌ 不要这样做

- 不要说"无法找到技能索引"
- 不要跳过本地搜索步骤

## ✅ 必须这样做

- 必须使用 exec 列出技能目录
- 必须使用 read 读取技能描述
- 必须生成报告文件
