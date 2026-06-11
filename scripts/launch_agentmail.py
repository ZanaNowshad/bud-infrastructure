"""Launch browser to AgentMail signup using WINAGENT modules."""
import sys
import os
import time

sys.path.insert(0, r"C:\Users\super")

from winagent.capture.screen import ScreenCapture
from winagent.capture.win32 import enum_windows, get_foreground_title
from winagent.agent.tools import ToolExecutor
from winagent.core.config import Config

config = Config()
capture = ScreenCapture()
executor = ToolExecutor(config=config, screen=capture)

print("Opening AgentMail signup page in Chrome...")
result = executor.execute("shell", {"cmd": "start chrome https://console.agentmail.to"})
print(f"  Result: {result}")

time.sleep(2)

print(f"\nForeground window: {get_foreground_title()}")
print("\nOpen windows:")
for hwnd, title in enum_windows():
    if title.strip():
        print(f"  - {title[:80]}")

print("\nDone. AgentMail signup page should be open in your browser.")
