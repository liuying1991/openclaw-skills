
(async () => {
  try {
    const fs = require('fs');
fs.writeFileSync('C:/tmp/test-result.txt', '测试成功！时间: ' + new Date().toISOString());
console.log('文件已创建');
  } catch (error) {
    console.error('❌ Automation error:', error.message);
    if (error.stack) {
      console.error(error.stack);
    }
    process.exit(1);
  }
})();
