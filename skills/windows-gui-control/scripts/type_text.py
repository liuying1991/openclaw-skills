import pyautogui
import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python type_text.py <text>")
    sys.exit(1)

text = sys.argv[1]

try:
    import pyperclip
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    print(f"Typed via clipboard: {text}")
except ImportError:
    subprocess.run(['powershell', '-command', f'Set-Clipboard -Value "{text}"'])
    pyautogui.hotkey('ctrl', 'v')
    print(f"Typed via PowerShell clipboard: {text}")
