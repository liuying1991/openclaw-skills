import pyautogui
import sys
import os
import json
import base64
from io import BytesIO

def take_screenshot():
    screenshot = pyautogui.screenshot()
    save_path = os.path.expanduser("~/.openclaw/workspace/skills/windows-gui-control/last_screenshot.png")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    screenshot.save(save_path)
    
    buffer = BytesIO()
    screenshot.save(buffer, format='PNG')
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    width, height = screenshot.size
    result = {
        "status": "success",
        "save_path": save_path,
        "width": width,
        "height": height,
        "base64_length": len(img_base64)
    }
    print(json.dumps(result))
    return result

def move_mouse(x, y):
    pyautogui.moveTo(int(x), int(y), duration=0.3)
    result = {"status": "success", "action": "move", "x": int(x), "y": int(y)}
    print(json.dumps(result))
    return result

def click(x, y, button='left', clicks=1):
    pyautogui.click(int(x), int(y), clicks=int(clicks), button=button)
    result = {"status": "success", "action": "click", "x": int(x), "y": int(y), "button": button, "clicks": int(clicks)}
    print(json.dumps(result))
    return result

def type_text(text):
    import pyperclip
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    result = {"status": "success", "action": "type", "text_length": len(text)}
    print(json.dumps(result))
    return result

def press_key(key):
    if '+' in key:
        keys = key.split('+')
        pyautogui.hotkey(*keys)
    else:
        pyautogui.press(key)
    result = {"status": "success", "action": "key", "key": key}
    print(json.dumps(result))
    return result

def scroll(direction, amount=3):
    if direction == 'up':
        pyautogui.scroll(int(amount) * 100)
    else:
        pyautogui.scroll(-int(amount) * 100)
    result = {"status": "success", "action": "scroll", "direction": direction, "amount": int(amount)}
    print(json.dumps(result))
    return result

def get_mouse_position():
    x, y = pyautogui.position()
    result = {"status": "success", "action": "position", "x": x, "y": y}
    print(json.dumps(result))
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "No action specified"}))
        sys.exit(1)
    
    action = sys.argv[1]
    
    try:
        if action == "screenshot":
            take_screenshot()
        elif action == "move":
            if len(sys.argv) < 4:
                print(json.dumps({"status": "error", "message": "Usage: gui_control.py move <x> <y>"}))
                sys.exit(1)
            move_mouse(sys.argv[2], sys.argv[3])
        elif action == "click":
            if len(sys.argv) < 4:
                print(json.dumps({"status": "error", "message": "Usage: gui_control.py click <x> <y> [button] [clicks]"}))
                sys.exit(1)
            button = sys.argv[4] if len(sys.argv) > 4 else 'left'
            clicks = sys.argv[5] if len(sys.argv) > 5 else 1
            click(sys.argv[2], sys.argv[3], button, clicks)
        elif action == "type":
            if len(sys.argv) < 3:
                print(json.dumps({"status": "error", "message": "Usage: gui_control.py type <text>"}))
                sys.exit(1)
            type_text(sys.argv[2])
        elif action == "key":
            if len(sys.argv) < 3:
                print(json.dumps({"status": "error", "message": "Usage: gui_control.py key <key>"}))
                sys.exit(1)
            press_key(sys.argv[2])
        elif action == "scroll":
            if len(sys.argv) < 3:
                print(json.dumps({"status": "error", "message": "Usage: gui_control.py scroll <direction> [amount]"}))
                sys.exit(1)
            amount = sys.argv[3] if len(sys.argv) > 3 else 3
            scroll(sys.argv[2], amount)
        elif action == "position":
            get_mouse_position()
        else:
            print(json.dumps({"status": "error", "message": f"Unknown action: {action}"}))
            sys.exit(1)
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)
