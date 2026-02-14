---
name: knowledge-organizer
description: Collect, organize, and summarize knowledge from multiple sources. Can search, extract, categorize, and create structured knowledge reports.
allowed-tools: Bash
---

# Knowledge Organizer Skill

Collect, organize, and summarize knowledge from multiple sources.

## Capabilities

- Search and collect information from web
- Extract key points from search results
- Categorize and organize information
- Create structured knowledge reports
- Save reports to files

## Workflow

### Step 1: Search
```
Action: searxng-search
Query: "topic to research"
Result: List of search results
```

### Step 2: Extract
```
Action: Extract key information from each result
- Title
- URL
- Summary
- Key points
```

### Step 3: Categorize
```
Action: Group information by category
- Beginner tutorials
- Advanced topics
- Best practices
- Tools and libraries
```

### Step 4: Create Report
```
Action: Generate structured report
- Overview
- Categories
- Key findings
- Sources
```

### Step 5: Save
```
Action: clawdbot-filesystem
Save report to markdown file
```

## Usage

### Complete Knowledge Collection
```
User: "帮我收集 Python 编程知识并整理成报告"

Execution Flow:
1. Search: searxng-search "Python编程入门教程"
2. Search: searxng-search "Python最佳实践"
3. Search: searxng-search "Python常用库"
4. Extract: Get key points from results
5. Categorize: Group by topic
6. Report: Create structured markdown
7. Save: Write to knowledge-report.md
```

## Report Template

```markdown
# [Topic] 知识报告

## 概述
[Brief overview of the topic]

## 分类知识

### 入门基础
- [Point 1]
- [Point 2]

### 进阶内容
- [Point 1]
- [Point 2]

### 最佳实践
- [Point 1]
- [Point 2]

## 推荐资源
1. [Title](URL) - [Description]
2. [Title](URL) - [Description]

## 总结
[Summary of key findings]

---
生成时间: [Timestamp]
来源: SearXNG 搜索引擎
```

## Examples

**Example 1: Programming Tutorial**
```
User: "收集 Python 教程知识"
Result: 
- 搜索 3 个相关主题
- 提取 15 条关键信息
- 分类整理
- 生成报告保存
```

**Example 2: Technology Research**
```
User: "研究人工智能发展趋势"
Result:
- 搜索 AI 最新动态
- 收集技术文章
- 整理发展趋势
- 生成研究报告
```

## Integration with Other Skills

| 技能 | 用途 |
|------|------|
| searxng-search | 搜索信息 |
| playwright-browser | 访问网页获取详细内容 |
| clawdbot-filesystem | 保存报告文件 |
| clipboard-control | 复制内容 |

## Best Practices

1. 使用多个搜索词获取全面信息
2. 验证信息来源的可靠性
3. 按逻辑分类整理知识
4. 提供原始来源链接
5. 定期更新知识库
