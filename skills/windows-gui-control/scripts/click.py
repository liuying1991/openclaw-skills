import pyautogui
import sys

if len(sys.argv) < 3:
    print("Usage: python click.py <x> <y> [button] [clicks]")
    sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])
button = sys.argv[3] if len(sys.argv) > 3 else 'left'
clicks = int(sys.argv[4]) if len(sys.argv) > 4 else 1

pyautogui.click(x, y, clicks=clicks, button=button)
print(f"Clicked {button} at ({x}, {y}) x{clicks}")
