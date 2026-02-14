---
name: task-agent
description: 子任务代理调度能力。用于启动独立的Agent执行子任务，支持并行执行多个任务。当需要并行处理或委托子任务时使用。
---

# Task Agent - 子任务代理调度

## 功能说明

这是一个强大的任务调度工具，用于：
- 启动独立的 Agent 执行子任务
- 并行处理多个任务
- 委托复杂任务给专门的 Agent
- 收集和整合多个 Agent 的结果

## 使用方法

### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| subagent_type | string | Agent 类型（如 search） |
| description | string | 任务描述（3-5个词） |
| query | string | 具体任务内容 |
| response_language | string | 返回语言 |

## 使用示例

### 搜索任务

```json
{
  "subagent_type": "search",
  "description": "搜索代码库中的认证逻辑",
  "query": "查找项目中处理用户认证的代码",
  "response_language": "zh-CN"
}
```

### 并行执行多个任务

可以同时启动多个 Agent：
- Agent 1: 搜索前端代码
- Agent 2: 搜索后端代码
- Agent 3: 搜索配置文件

## 最佳实践

1. **明确任务目标** - query 要清晰具体
2. **合理并行** - 独立任务可以并行
3. **结果整合** - 收集所有 Agent 结果后整合
4. **错误处理** - 单个 Agent 失败不影响其他

## 适用场景

- 大规模代码搜索
- 多文件并行处理
- 复杂任务分解
- 独立子任务执行
