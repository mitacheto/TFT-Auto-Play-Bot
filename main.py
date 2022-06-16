import pyautogui
from time import sleep
from scanner import scan_screen

def start():
    while True:
        found = scan_screen()
        if found:
            if found[1].amount > 0:
                pyautogui.moveTo(found[0][0] + 50, found[0][1] - 100)
                sleep(1)
start()
