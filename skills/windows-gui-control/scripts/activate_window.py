import subprocess
import sys
import time

if len(sys.argv) < 2:
    print("Usage: python activate_window.py <title>")
    sys.exit(1)

title = sys.argv[1]

ps_script = f'''
Add-Type @"
  using System;
  using System.Runtime.InteropServices;
  public class Win32 {{
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hWnd);
  }}
"@

$process = Get-Process | Where-Object {{ $_.MainWindowTitle -like "*{title}*" }} | Select-Object -First 1
if ($process) {{
    [Win32]::SetForegroundWindow($process.MainWindowHandle)
    Write-Host "Activated window: {title}"
}} else {{
    Write-Host "Window not found: {title}"
}}
'''

result = subprocess.run(['powershell', '-command', ps_script], capture_output=True, text=True)
print(result.stdout.strip())
if result.stderr:
    print(f"Error: {result.stderr.strip()}")
