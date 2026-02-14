---
name: error-recovery
description: 错误恢复机制。当任务执行失败时，自动诊断错误原因并尝试恢复。支持重试、回滚、替代方案。
allowed-tools: All
---

# Error Recovery - 错误恢复机制

**任务失败时自动诊断并恢复**

---

## 🎯 错误类型分类

| 错误类型 | 说明 | 恢复策略 |
|----------|------|----------|
| **网络错误** | 连接超时、服务不可用 | 重试、切换服务 |
| **权限错误** | 权限不足、访问被拒 | 请求权限、使用 sudo |
| **资源错误** | 文件不存在、内存不足 | 创建资源、释放内存 |
| **语法错误** | 命令错误、参数错误 | 修正命令、查阅文档 |
| **服务错误** | 服务未启动、端口占用 | 启动服务、更换端口 |

---

## 🔄 错误恢复流程

```
任务执行
    │
    ├─ 成功 → 返回结果
    │
    └─ 失败 → 错误诊断
              │
              ├─ 识别错误类型
              │   ├─ 网络错误 → 重试(最多3次)
              │   ├─ 权限错误 → 使用 sudo/请求权限
              │   ├─ 资源错误 → 创建/释放资源
              │   ├─ 语法错误 → 修正命令
              │   └─ 服务错误 → 启动服务
              │
              ├─ 尝试恢复
              │   ├─ 成功 → 继续任务
              │   └─ 失败 → 尝试替代方案
              │
              └─ 替代方案
                  ├─ 成功 → 返回结果
                  └─ 失败 → 报告用户
```

---

## 📋 常见错误恢复方案

### 1. 网络错误

```powershell
# 错误: 连接超时
# 恢复: 重试 + 增加超时时间

# 第1次尝试
Invoke-WebRequest -Uri "http://localhost:8080" -TimeoutSec 5

# 失败后重试
Invoke-WebRequest -Uri "http://localhost:8080" -TimeoutSec 10

# 仍然失败 → 启动服务
wsl -d Ubuntu-22.04 -e bash -c "python3 searx/webapp.py &"
```

### 2. 权限错误

```powershell
# 错误: 权限不足
# 恢复: 使用 sudo

# 第1次尝试
wsl -d Ubuntu-22.04 -e bash -c "service docker start"

# 失败后使用 sudo
wsl -d Ubuntu-22.04 -e bash -c "echo '1991' | sudo -S service docker start"
```

### 3. 服务错误

```powershell
# 错误: 服务未运行
# 恢复: 启动服务

# 检查服务
Invoke-WebRequest -Uri "http://localhost:8080" -UseBasicParsing

# 失败 → 启动服务
wsl -d Ubuntu-22.04 -e bash -c "cd /home/liuying/searxng && python3 searx/webapp.py &"
Start-Sleep -Seconds 5

# 再次检查
Invoke-WebRequest -Uri "http://localhost:8080" -UseBasicParsing
```

### 4. 文件错误

```powershell
# 错误: 文件不存在
# 恢复: 创建文件或使用替代路径

# 第1次尝试
Get-Content "C:\path\to\file.txt"

# 失败 → 检查替代路径
Get-Content "C:\alternative\path\file.txt"

# 仍然失败 → 创建文件
New-Item -Path "C:\path\to\file.txt" -ItemType File
```

---

## 🔄 重试策略

| 错误类型 | 重试次数 | 重试间隔 | 说明 |
|----------|----------|----------|------|
| 网络错误 | 3 次 | 递增 (1s, 2s, 4s) | 等待网络恢复 |
| 服务错误 | 2 次 | 5 秒 | 等待服务启动 |
| 权限错误 | 1 次 | 立即 | 使用 sudo |
| 其他错误 | 1 次 | 立即 | 尝试替代方案 |

---

## 📊 替代方案库

| 原方案 | 替代方案 1 | 替代方案 2 |
|--------|------------|------------|
| SearXNG 搜索 | WebSearch 工具 | WebFetch 直接获取 |
| Playwright 获取 | curl 命令 | Invoke-WebRequest |
| WSL 命令 | PowerShell 命令 | cmd 命令 |
| 本地服务 | 在线 API | 缓存数据 |

---

## 💡 错误预防

### 1. 执行前检查

```powershell
# 检查服务状态
if (-not (Test-Service "SearXNG")) {
    Start-Service "SearXNG"
}

# 检查文件存在
if (-not (Test-Path "file.txt")) {
    New-Item "file.txt"
}

# 检查网络连接
if (-not (Test-Connection "localhost:8080")) {
    Start-Sleep -Seconds 5
}
```

### 2. 超时设置

```powershell
# 设置合理的超时时间
$timeout = 10  # 秒

# 使用超时
Invoke-WebRequest -Uri $url -TimeoutSec $timeout
```

### 3. 错误日志

```powershell
# 记录错误
try {
    # 执行任务
} catch {
    $errorLog = @{
        Time = Get-Date
        Task = $taskName
        Error = $_.Exception.Message
        Recovery = $recoveryAction
    }
    Add-Content "error.log" ($errorLog | ConvertTo-Json)
}
```

---

## 📋 错误恢复检查清单

- [ ] 识别错误类型
- [ ] 尝试重试 (最多 3 次)
- [ ] 尝试替代方案
- [ ] 记录错误日志
- [ ] 通知用户 (如果无法恢复)

---

**错误恢复机制让 OpenClaw 更加健壮！**
