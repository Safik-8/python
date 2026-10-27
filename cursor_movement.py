# cursor_movement.py
import time
import pyautogui

pyautogui.FAILSAFE = True  # Move mouse to top-left corner to immediately stop

time.sleep(3)  # Time to switch to the target window

# Move cursor through a few screen positions
pyautogui.moveTo(200, 200, duration=1)
pyautogui.moveTo(800, 200, duration=1)
pyautogui.moveTo(800, 600, duration=1)
pyautogui.moveTo(200, 600, duration=1)
pyautogui.moveTo(500, 400, duration=1)