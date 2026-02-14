---
name: auto-service-manager
description: Automatically check and start required services (WSL, SearXNG, Playwright) when needed. Can handle password input for Linux. Read credentials from SYSTEM_CREDENTIALS.md.
allowed-tools: Bash, keyboard-control
---

# Auto Service Manager - 自动服务管理器

当 OpenClaw 需要使用网络搜索功能时，自动检测并启动所需服务。

## 🔐 密码存储位置

密码存储在: `~/.openclaw/workspace/SYSTEM_CREDENTIALS.md`

```
Linux 密码: 1991
WSL 发行版: Ubuntu-22.04
```

## 🎯 自动启动流程

### 步骤1：检查 WSL 是否运行

```powershell
wsl -d Ubuntu-22.04 -e bash -c "echo 'checking'"
```

如果失败，说明 WSL 未启动，需要启动 WSL。

### 步骤2：启动 WSL（如果需要）

如果 WSL 未运行，执行：

```powershell
wsl -d Ubuntu-22.04
```

**如果需要输入密码**，使用键盘控制输入密码 `1991`

### 步骤3：检查 SearXNG 是否运行

```powershell
Invoke-WebRequest -Uri "http://localhost:8080" -UseBasicParsing -TimeoutSec 5
```

如果失败，启动 SearXNG：

```powershell
wsl -d Ubuntu-22.04 -e bash -c "echo '1991' | sudo -S service docker start && export SEARXNG_SETTINGS_PATH=/home/liuying/.config/searxng/settings.yml && cd /home/liuying/searxng && nohup python3 searx/webapp.py > /home/liuying/searxng.log 2>&1 &"
```

### 步骤4：验证服务

等待 5 秒后验证：

```powershell
Start-Sleep -Seconds 5
Invoke-WebRequest -Uri "http://localhost:8080" -UseBasicParsing -TimeoutSec 5
```

## 📋 完整自动检测脚本

当用户请求网络搜索时，按以下顺序执行：

```
1. 检查 WSL
   → 如果失败，启动 WSL
   → 如果需要密码，自动输入 "1991"

2. 检查 SearXNG
   → 如果失败，启动 SearXNG（使用密码 1991）

3. 等待服务启动
   → 最多等待 10 秒

4. 验证服务可用
   → 确认可以访问 http://localhost:8080

5. 执行搜索任务
```

## ⚠️ 重要提示

1. **密码安全** - 密码存储在本地文件，不要上传到云端
2. **自动输入** - 如果需要交互式输入密码，使用键盘控制工具
3. **等待时间** - 服务启动需要时间，要等待后再验证

## 🔧 键盘控制输入密码

如果 WSL 启动时需要密码，使用以下方式：

```powershell
# 方法1：直接通过管道输入
echo "1991" | wsl -d Ubuntu-22.04 -e bash -c "sudo -S command"

# 方法2：使用键盘控制
# 1. 启动 WSL
# 2. 等待密码提示
# 3. 发送键盘输入 "1991"
# 4. 发送 Enter 键
```

## 📝 凭证信息

| 项目 | 值 |
|------|------|
| Linux 密码 | 1991 |
| WSL 发行版 | Ubuntu-22.04 |
| SearXNG 端口 | 8080 |
| Playwright 路径 | /home/liuying/web-tools |
