---
name: playwright-browser
description: 使用 Playwright 自动化浏览器。执行方式：1. write 创建脚本到 C:\tmp\xxx.js 2. exec 执行：node C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\playwright-browser\run.js C:\tmp\xxx.js 3. exec 验证文件存在
allowed-tools: Bash
---

# Playwright 浏览器自动化技能

## ⚠️ 执行方式 - 必须按此步骤

### 步骤 1：创建脚本
使用 `write` 工具创建脚本到 `C:\tmp\script.js`

### 步骤 2：执行脚本
使用 `exec` 工具执行：
```
node C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\playwright-browser\run.js C:\tmp\script.js
```

### 步骤 3：验证结果
使用 `exec` 工具检查文件：
```
dir C:\tmp\结果文件名
```

---

## 脚本模板

```javascript
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  
  // 打开网页
  await page.goto('https://www.bing.com', { waitUntil: 'networkidle' });
  console.log('标题:', await page.title());
  
  // 搜索
  await page.evaluate(() => {
    document.querySelector('#sb_form_q').value = '搜索内容';
    document.querySelector('#sb_form').submit();
  });
  
  // 等待
  await page.waitForTimeout(5000);
  
  // 截图
  await page.screenshot({ path: 'C:/tmp/screenshot.png', fullPage: true });
  console.log('截图已保存');
  
  await browser.close();
})();
```

---

## 完整示例

**任务：搜索并截图**

1. **write** 创建 `C:\tmp\search.js`：
```javascript
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.goto('https://www.bing.com', { waitUntil: 'networkidle' });
  await page.evaluate(() => {
    document.querySelector('#sb_form_q').value = 'OpenClaw';
    document.querySelector('#sb_form').submit();
  });
  await page.waitForTimeout(5000);
  await page.screenshot({ path: 'C:/tmp/result.png', fullPage: true });
  console.log('完成');
  await browser.close();
})();
```

2. **exec** 执行：
```
node C:\Users\Administrator.WIN-15VSDGCVDE6\.openclaw\workspace\skills\playwright-browser\run.js C:\tmp\search.js
```

3. **exec** 验证：
```
dir C:\tmp\result.png
```

---

## 常用选择器

| 网站 | 搜索框 | 搜索表单 |
|------|--------|----------|
| Bing | `#sb_form_q` | `#sb_form` |
| Baidu | `#kw` | `#form` |
| Google | `input[name="q"]` | `form` |

---

## ❌ 不要这样做

- 不要使用 Chrome 扩展
- 不要等待用户操作
- 不要只生成代码不执行

## ✅ 必须这样做

- 必须使用 write 创建脚本
- 必须使用 exec 执行脚本
- 必须使用 exec 验证文件
