# Data Report Generator (data-report-generator)

## 技能描述
`data-report-generator` 是一款可以 **自动读取 CSV、JSON、Excel** 数据文件，进行基础统计分析（均值、中位数、标准差等），并 **生成 Markdown 报告** 的工具。报告中包含数据概览、统计表格以及可视化的 ASCII/文本图表，适合在聊天窗口、文档或 CI 中直接展示。

## 支持的数据源
- **CSV**（逗号分隔，UTF‑8 编码）
- **JSON**（数组形式的对象列表）
- **Excel**（`.xlsx` / `.xls`，默认读取第一个工作表）

## 输出格式
- **Markdown** 文本，包含标题、表格、代码块等。
- 图表采用 **ASCII 条形图** 或 **简单折线描述**，不依赖外部图片。用户可以自行替换为实际图片链接。

## 使用方法
```text
!skill data-report-generator "<data_file_path>" [options]
```
- `<data_file_path>` 必填，指向本地数据文件的绝对路径或相对路径。
- `options`（可选）用空格分隔的键值对，常用如下：
  - `summary:true|false`  是否生成数据摘要（默认 true）
  - `stats:col1,col2,...`  指定要统计的列名，若省略则统计所有数值列
  - `chart:col`            为指定列生成 ASCII 条形图（默认不生成）
  - `title:"Report Title"` 自定义报告标题

### 示例
```text
!skill data-report-generator "C:/data/sales.xlsx" summary:true chart:Revenue title:"2025 销售报告"
```
会得到类似下面的 Markdown 报告：

## 示例报告（Markdown）
```markdown
# 2025 销售报告

## 数据概览
- 数据来源：`C:/data/sales.xlsx`
- 行数： 1200
- 列数： 8

## 统计指标
| 列名      | 均值   | 中位数 | 标准差 |
|-----------|-------|-------|-------|
| Revenue   | 10423 | 9800  | 2150  |
| UnitsSold | 352   | 300   | 45    |

## ASCII 条形图 – Revenue
```
Revenue
 ├─  0 - 5k   : ████
 ├─  5k-10k   : ██████████
 ├─ 10k-15k   : ███████
 └─ 15k+      : ███
```

## 数据摘要
> 本报告基于 2025 年 1‑12 月的销售数据进行分析，整体收入呈上升趋势，第二季度出现显著增长。详细的月份趋势请参考原始 Excel 表格。
```

## 配置选项（可在 `config.json` 中预设）
```json
{
  "default_summary": true,
  "default_chart": false,
  "default_title": "Data Report",
  "number_format": "0,0.00"
}
```

## 实现要点（供开发者参考）
1. **读取文件**：使用 Python 的 `pandas.read_csv`、`pandas.read_json`、`pandas.read_excel` 自动识别文件类型。
2. **统计指标**：利用 `pandas.mean`、`pandas.median`、`pandas.std` 计算每列的均值/中位数/标准差。
3. **ASCII 图表**：根据数值范围把数据分桶，使用 Unicode 块元素 `█` 绘制条形图；也可以使用 `matplotlib` 生成 SVG/PNG，随后返回图片的 Data URL（可选功能）。
4. **Markdown 渲染**：拼装标题、表格、代码块等字符串并返回给 OpenClaw 框架，由平台直接展示。
5. **异常处理**：如果文件不存在、格式不支持或列中无数值，则返回友好的错误提示。

---
*本技能遵循 OpenClaw 插件规范，放置于 `workspace/skills/data-report-generator` 目录下即可使用。*