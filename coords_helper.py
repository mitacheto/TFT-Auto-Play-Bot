import pyautogui

iml = pyautogui.screenshot(region=(635, 1225, 1340, 210))
iml.save('screenshot.png')