---
name: sequential-thinking
description: 深度思考和问题分析能力。用于复杂问题分析、多步骤推理、假设验证。当需要深入思考问题时使用。
---

# Sequential Thinking - 深度思考能力

## 功能说明

这是一个强大的深度思考工具，用于：
- 复杂问题分析
- 多步骤推理
- 假设生成与验证
- 问题分解与解决

## 使用方法

### 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| thought | string | 当前思考步骤 |
| thoughtNumber | integer | 当前思考步骤编号 |
| totalThoughts | integer | 预计总思考步骤数 |
| nextThoughtNeeded | boolean | 是否需要继续思考 |
| isRevision | boolean | 是否是修正之前的思考 |
| branchFromThought | integer | 分支起点（可选） |
| branchId | string | 分支标识（可选） |
| needsMoreThoughts | boolean | 是否需要更多思考 |

## 使用示例

### 基本用法

```json
{
  "thought": "分析问题的第一步：理解问题的核心是什么...",
  "thoughtNumber": 1,
  "totalThoughts": 5,
  "nextThoughtNeeded": true
}
```

### 修正之前的思考

```json
{
  "thought": "重新考虑之前的假设，发现新的可能性...",
  "thoughtNumber": 3,
  "totalThoughts": 6,
  "isRevision": true,
  "revisesThought": 2,
  "nextThoughtNeeded": true
}
```

### 分支思考

```json
{
  "thought": "探索一个替代方案...",
  "thoughtNumber": 4,
  "totalThoughts": 8,
  "branchFromThought": 3,
  "branchId": "alternative-approach",
  "nextThoughtNeeded": true
}
```

## 最佳实践

1. **从问题理解开始** - 第一步总是理解问题
2. **分解复杂问题** - 将大问题分解为小步骤
3. **验证假设** - 每个假设都要验证
4. **允许回溯** - 发现错误时可以修正
5. **生成结论** - 最后一步给出最终答案

## 适用场景

- 复杂算法设计
- 系统架构分析
- 问题根因分析
- 多方案对比
- 决策支持
