import pyautogui
import sys

if len(sys.argv) < 2:
    print("Usage: python scroll.py <direction> [amount]")
    sys.exit(1)

direction = sys.argv[1]
amount = int(sys.argv[2]) if len(sys.argv) > 2 else 3

if direction == 'up':
    pyautogui.scroll(amount * 100)
    print(f"Scrolled up {amount} times")
elif direction == 'down':
    pyautogui.scroll(-amount * 100)
    print(f"Scrolled down {amount} times")
else:
    print(f"Unknown direction: {direction}")
