import pyautogui
import base64
from io import BytesIO
import os

screenshot = pyautogui.screenshot()
save_path = os.path.expanduser("~/.openclaw/workspace/skills/windows-gui-control/last_screenshot.png")
screenshot.save(save_path)

buffer = BytesIO()
screenshot.save(buffer, format='PNG')
img_base64 = base64.b64encode(buffer.getvalue()).decode()

width, height = screenshot.size
print(f"SCREENSHOT_SAVED: {save_path}")
print(f"SCREEN_SIZE: {width}x{height}")
print(f"SCREENSHOT_BASE64:{img_base64[:100]}...")
