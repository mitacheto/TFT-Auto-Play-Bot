import cv2 as cv
from cv2 import log
import numpy as np
from time import sleep, time
from gamecampture import GameCapture
from vision import Vision
import pyautogui
from threading import Thread
from comp import generateComp

gamecap = GameCapture()
GameCapture.list_window_names()
is_bot_in_action = False

def bot_actions(rectangles,champs):
    if len(rectangles) > 0:
        targets = champs.get_click_points(rectangles)
        target = gamecap.get_screen_position(targets[0])
        pyautogui.moveTo(x=target[0], y=target[1])
        sleep(1)
        pyautogui.click()

loop_time = time()
while(True):
    screenshot = gamecap.gamewindow_capture()

    composition = generateComp()

    for champs in composition:
        rectangles = champs.find(screenshot, 0.5)
        output_image = champs.draw_rectangles(screenshot, rectangles)
        cv.imshow('Matches', output_image)
        if not is_bot_in_action:
            is_bot_in_action = True
            t = Thread(target=bot_actions, args=(rectangles, champs))
            t.start()

    

    # print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    if(cv.waitKey(1) == ord('q')):
        cv.destroyAllWindows()
        break


print("Done")
