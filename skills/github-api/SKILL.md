---
name: github-api
description: GitHub API 访问能力。用于获取仓库信息、用户信息、搜索代码等。执行命令：node C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\github-api\scripts\github-api.js <command> [args]
---

# GitHub API 技能

## 功能说明

访问 GitHub API 获取：
- 仓库信息（stars、forks、issues）
- 用户信息
- 热门仓库
- 搜索仓库

## 使用方法

### 获取仓库信息
```bash
node C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\github-api\scripts\github-api.js repo <owner> <repo>
```

示例：
```bash
node ... github-api.js repo microsoft vscode
```

### 获取用户信息
```bash
node ... github-api.js user <username>
```

### 获取热门仓库
```bash
node ... github-api.js trending
```

### 搜索仓库
```bash
node ... github-api.js search <query>
```

## 返回格式

所有命令返回 JSON 格式数据。

## 配置文件

Token 配置在：`config/api-keys.json`
