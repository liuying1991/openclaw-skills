---
name: learning-memory
description: 学习记忆系统。自动记录任务执行经验，提取关键知识，持续优化执行效率。支持经验积累、知识检索、自动优化。
allowed-tools: All
---

# Learning Memory - 学习记忆系统

**自动记录经验，持续优化效率**

---

## 🎯 系统架构

```
任务执行
    │
    ├─ 执行前 → 检索相关经验
    │
    ├─ 执行中 → 应用已知方案
    │
    └─ 执行后 → 记录新经验
                │
                ├─ 成功经验 → 存入知识库
                ├─ 失败经验 → 记录避坑指南
                └─ 优化建议 → 更新执行方案
```

---

## 📁 记忆存储结构

### 1. 经验记录格式

```markdown
## [日期] [任务类型] - [任务描述]

### 执行方案
1. 步骤1
2. 步骤2
3. 步骤3

### 执行结果
- 状态: 成功/失败
- 耗时: XX秒
- 关键点: XXX

### 经验总结
- 成功因素: XXX
- 避坑指南: XXX
- 优化建议: XXX
```

### 2. 知识库文件

| 文件 | 内容 | 更新频率 |
|------|------|----------|
| `EXPERIENCE.md` | 核心经验知识库 | 每次重要任务后 |
| `MEMORY.md` | 长期记忆 | 每周 |
| `memory/YYYY-MM-DD.md` | 每日工作记录 | 每天 |
| `skills/*/SKILL.md` | 技能知识 | 按需 |

---

## 🔄 学习流程

### 1. 任务执行前

```
1. 分析任务类型
2. 检索相关经验
   ├─ 搜索 EXPERIENCE.md
   ├─ 搜索 MEMORY.md
   └─ 搜索相关 SKILL.md
3. 应用已知方案
4. 如果没有经验 → 使用默认方案
```

### 2. 任务执行后

```
1. 记录执行结果
2. 分析成功/失败原因
3. 提取关键经验
4. 更新知识库
   ├─ 更新 EXPERIENCE.md
   ├─ 更新 memory/YYYY-MM-DD.md
   └─ 更新相关 SKILL.md (如有重大发现)
```

---

## 📊 经验分类

### 1. 按任务类型

| 类型 | 经验文件 | 示例 |
|------|----------|------|
| 网络搜索 | EXPERIENCE.md#web-search | 搜索技巧、避坑指南 |
| 电脑操控 | COMPUTER_CONTROL.md | 快捷键、操作技巧 |
| 服务管理 | EXPERIENCE.md#service | 启动命令、故障排除 |
| Trae IDE | skills/trae-cn-ide/SKILL.md | 使用技巧、操控方法 |

### 2. 按经验类型

| 类型 | 说明 | 存储位置 |
|------|------|----------|
| 成功方案 | 验证有效的执行方案 | EXPERIENCE.md |
| 避坑指南 | 常见错误及解决方案 | EXPERIENCE.md |
| 优化建议 | 提升效率的方法 | EXPERIENCE.md |
| 快速命令 | 常用命令速查 | MEMORY.md |

---

## 💡 经验提取规则

### 1. 成功经验提取

```
如果任务成功:
1. 记录执行方案
2. 记录关键步骤
3. 记录耗时
4. 提取可复用的模式
```

### 2. 失败经验提取

```
如果任务失败:
1. 记录错误类型
2. 记录错误原因
3. 记录解决方案
4. 添加到避坑指南
```

### 3. 优化建议提取

```
如果发现更好的方法:
1. 对比新旧方法
2. 记录改进点
3. 更新知识库
```

---

## 📋 经验模板

### 网络搜索经验

```markdown
## Web Search Experience

### Quick Commands
```powershell
# Search
Invoke-WebRequest -Uri 'http://localhost:8080/search?q=TERM&format=json'

# Fetch
wsl node playwright_fetcher.js URL
```

### Success Factors
1. Check service first
2. Use URL encoding for Chinese
3. Limit to 3-5 URLs

### Pitfalls to Avoid
1. Don't use built-in web_fetch
2. Don't forget to check service status
3. Don't fetch too many URLs
```

### 电脑操控经验

```markdown
## Computer Control Experience

### Key Principles
1. Delay is critical - 操作之间必须有延迟
2. Window must be active - 窗口必须激活
3. Use Tab navigation - Tab 导航最可靠

### Quick Commands
```powershell
# Keyboard
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("text")

# Mouse
[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(X, Y)
```
```

---

## 🔍 知识检索

### 1. 检索优先级

```
1. EXPERIENCE.md (核心经验)
2. MEMORY.md (长期记忆)
3. skills/*/SKILL.md (技能知识)
4. memory/YYYY-MM-DD.md (近期记录)
```

### 2. 检索关键词

| 任务类型 | 检索关键词 |
|----------|------------|
| 网络搜索 | web, search, fetch, searxng, playwright |
| 电脑操控 | keyboard, mouse, window, control |
| 服务管理 | service, start, docker, wsl |
| Trae IDE | trae, solo, builder, plan |

---

## 📊 学习效果评估

| 指标 | 说明 | 目标 |
|------|------|------|
| 任务执行时间 | 同类任务耗时 | 逐渐减少 |
| 错误率 | 同类任务失败率 | 逐渐降低 |
| 复用率 | 使用已知方案的比例 | 逐渐提高 |
| 知识库大小 | 经验记录数量 | 持续增长 |

---

## 💡 自动优化

### 1. 定期整理

```
每周:
1. 整理 memory/YYYY-MM-DD.md
2. 提取重要经验到 EXPERIENCE.md
3. 删除过时信息
4. 更新知识索引
```

### 2. 知识压缩

```
当知识库过大时:
1. 提取核心知识
2. 删除重复内容
3. 合并相似条目
4. 创建快速索引
```

---

**学习记忆系统让 OpenClaw 越用越聪明！**
