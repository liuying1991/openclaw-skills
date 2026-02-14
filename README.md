# OpenClaw Skills - 智能代理技能配置库

<div align="center">

![OpenClaw Logo](https://img.shields.io/badge/OpenClaw-AI%20Agent%20Skills-blue?style=for-the-badge)

**一个强大的 AI 智能代理技能系统**

[![GitHub stars](https://img.shields.io/github/stars/liuying1991/openclaw-skills?style=social)](https://github.com/liuying1991/openclaw-skills/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/liuying1991/openclaw-skills?style=social)](https://github.com/liuying1991/openclaw-skills/network/members)
[![License](https://img.shields.io/github/license/liuying1991/openclaw-skills)](LICENSE)

</div>

---

## 📖 项目简介

OpenClaw Skills 是一个模块化的 AI 智能代理技能配置系统。它允许 AI 助手通过技能模块来扩展其能力，实现更复杂、更智能的任务处理。

### 🎯 核心特性

- **模块化设计** - 每个技能独立配置，易于扩展和维护
- **智能执行** - 内置执行验证机制，确保任务真正完成
- **多技能协同** - 支持多个技能组合完成复杂任务
- **错误恢复** - 自动错误检测和恢复能力
- **知识管理** - 支持知识存储、检索和组织

---

## 🛠️ 技能列表

### 🧠 核心能力

| 技能 | 描述 |
|------|------|
| `sequential-thinking` | 深度思考和问题分析能力 |
| `task-agent` | 子任务代理调度，支持并行处理 |
| `code-analysis` | 代码分析和理解能力 |
| `multi-file-editor` | 多文件批量编辑能力 |
| `intelligent-planner` | 智能任务规划和分解 |
| `context-manager` | 上下文管理和记忆 |

### 🌐 浏览器自动化

| 技能 | 描述 |
|------|------|
| `playwright-browser` | Playwright 浏览器自动化 |
| `web-search` | 网络搜索能力 |

### 🖥️ 系统操作

| 技能 | 描述 |
|------|------|
| `windows-gui-control` | Windows GUI 自动化控制 |
| `auto-service-manager` | 自动化服务管理 |
| `software-operations` | 软件安装和配置 |
| `computer-use` | 电脑交互控制 |

### 📝 知识管理

| 技能 | 描述 |
|------|------|
| `knowledge-organizer` | 知识组织和分类 |
| `learning-memory` | 学习记忆系统 |
| `find-skills` | 技能搜索和发现 |

### ⚡ 任务管理

| 技能 | 描述 |
|------|------|
| `task-prioritizer` | 任务优先级分析 |
| `proactive-agent` | 主动代理和建议 |
| `error-recovery` | 错误恢复和重试 |

### 🔧 工具技能

| 技能 | 描述 |
|------|------|
| `clawdbot-filesystem` | 文件系统操作 |
| `cherry-studio` | 多模态内容生成 |
| `github-api` | GitHub API 访问 |
| `data-report-generator` | 数据报告生成 |

---

## 🚀 快速开始

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/liuying1991/openclaw-skills.git
```

2. 将技能目录复制到你的 OpenClaw 工作空间：
```bash
cp -r openclaw-skills/skills/* ~/.openclaw/workspace/skills/
cp openclaw-skills/*.md ~/.openclaw/workspace/
```

### 配置

1. 配置 API 密钥（可选）：
```json
// ~/.openclaw/workspace/config/api-keys.json
{
  "github": {
    "token": "your-github-token"
  }
}
```

2. 重启 OpenClaw 服务

---

## 📁 目录结构

```
openclaw-skills/
├── skills/                    # 技能模块目录
│   ├── playwright-browser/    # 浏览器自动化
│   ├── web-search/           # 网络搜索
│   ├── task-prioritizer/     # 任务优先级
│   ├── error-recovery/       # 错误恢复
│   ├── knowledge-organizer/  # 知识组织
│   ├── learning-memory/      # 学习记忆
│   ├── sequential-thinking/  # 深度思考
│   ├── task-agent/           # 任务代理
│   ├── code-analysis/        # 代码分析
│   ├── multi-file-editor/    # 多文件编辑
│   ├── intelligent-planner/  # 智能规划
│   ├── context-manager/      # 上下文管理
│   └── ...                   # 更多技能
├── AGENTS.md                 # Agent 执行规则
├── SOUL.md                   # 系统身份定义
├── EXECUTION_RULES.md        # 执行验证规则
├── IDENTITY.md               # 身份配置
└── README.md                 # 本文件
```

---

## 🔧 技能开发

### 创建新技能

1. 在 `skills/` 目录下创建新文件夹：
```bash
mkdir skills/my-skill
```

2. 创建技能配置文件 `SKILL.md`：
```markdown
---
name: my-skill
description: 我的自定义技能
---

# My Skill

## 功能说明
描述你的技能功能...

## 使用方法
说明如何使用...
```

3. 添加脚本文件（可选）

### 技能配置格式

```yaml
---
name: skill-name                    # 技能名称
description: 技能描述                # 简短描述
allowed-tools: Bash, exec           # 允许使用的工具
---
```

---

## 📋 执行规则

OpenClaw 采用严格的执行验证机制：

1. **必须真正执行** - 不能只生成代码不执行
2. **必须验证结果** - 检查文件是否存在
3. **必须返回真实数据** - 包含文件大小、时间等

详细规则请参考 [EXECUTION_RULES.md](EXECUTION_RULES.md)

---

## 🤝 贡献指南

欢迎贡献新技能或改进现有技能！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/new-skill`)
3. 提交更改 (`git commit -am 'Add new skill'`)
4. 推送到分支 (`git push origin feature/new-skill`)
5. 创建 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

感谢所有贡献者和开源社区的支持！

---

<div align="center">

**[⬆ 返回顶部](#openclaw-skills---智能代理技能配置库)**

Made with ❤️ by OpenClaw Team

</div>
