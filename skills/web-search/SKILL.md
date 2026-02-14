---
name: web-search
description: FAST web search using SearXNG + Playwright. Use this for ALL web search tasks. Auto-checks and starts services. Returns summarized results.
allowed-tools: Bash, exec
---

# 🔍 Web Search - 网络搜索

## ⚠️ 重要规则 - 必须遵守

1. **不能只生成代码，必须真正执行！**
2. **每一步都必须验证结果！**
3. **必须返回真实的搜索结果给用户！**

---

## Agent 执行流程（必须按顺序执行）

### 步骤 1：获取 WSL IP
使用 `exec` 工具执行：
```powershell
$wslIp = (wsl -d Ubuntu-22.04 -e bash -c "hostname -I").Trim().Split()[0]
Write-Host "WSL IP: $wslIp"
```

**验证**：确认输出了 IP 地址

### 步骤 2：检查服务
使用 `exec` 工具执行：
```powershell
$wslIp = (wsl -d Ubuntu-22.04 -e bash -c "hostname -I").Trim().Split()[0]
Invoke-WebRequest -Uri "http://${wslIp}:8080" -UseBasicParsing -TimeoutSec 5
```

**如果失败，执行：**
```powershell
wsl -d Ubuntu-22.04 -e bash -c "sudo systemctl restart searxng.service"
```

### 步骤 3：执行搜索
使用 `exec` 工具执行：
```powershell
$wslIp = (wsl -d Ubuntu-22.04 -e bash -c "hostname -I").Trim().Split()[0]
$searchUrl = "http://${wslIp}:8080/search?q=SEARCH_TERM&format=json&engines=bing"
$result = Invoke-WebRequest -Uri $searchUrl -UseBasicParsing
$result.Content
```

**验证**：确认返回了 JSON 数据

### 步骤 4：获取网页内容（可选）
使用 `exec` 工具执行：
```powershell
wsl -d Ubuntu-22.04 -e bash -c "node /home/liuying/web-tools/playwright_fetcher.js 'URL'"
```

### 步骤 5：总结结果
**必须**将搜索结果总结后返回给用户！

---

## 完整示例

**用户请求：** "搜索鸡蛋的营养信息"

**执行步骤：**

1. 获取 WSL IP
2. 检查服务
3. 搜索：`egg nutrition`
4. 获取前3个网页内容
5. 总结结果返回给用户

**必须返回真实的搜索结果，不能只说"已完成"！**

---

## 🔐 Password

```
Linux Password: 1991
sudo: 免密已配置
```

---

## 📊 Service Info

| Service | Address | Purpose |
|---------|---------|---------|
| SearXNG | http://WSL_IP:8080 | Search Engine |
| Playwright | /home/liuying/web-tools | Web Content Fetcher |

**Current WSL IP:** 172.27.171.188

---

## ❌ 错误示例（不要这样做）

```
错误：只生成代码，不执行
错误：只说"搜索完成"，不返回结果
错误：跳过服务检查
```

## ✅ 正确示例（必须这样做）

```
正确：获取IP → 检查服务 → 执行搜索 → 返回结果
正确：每一步都有输出确认
正确：返回真实的搜索结果给用户
```
