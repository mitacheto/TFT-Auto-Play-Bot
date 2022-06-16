import cv2 as cv
import dxcam
from comp import generate_champs

region = (635, 1225, 1340, 210)
camera = dxcam.create()
frame = camera.grab()  # region
camera.start(target_fps=60)  # threaded
champs = generate_champs()

def screen_capture():
    image = camera.get_latest_frame()
    return image;

def scan_screen():
    screen = screen_capture()
    for champ in champs:
        img = cv.imread(champ.imp_path, cv.IMREAD_COLOR)
        result = cv.matchTemplate(screen, img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if max_val > 0.8:
            return max_loc, champ
