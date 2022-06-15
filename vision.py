import cv2 as cv
import numpy as np

class Vision:

    champion_name_img = None
    champion_name_img_w = 0
    champion_name_img_h = 0
    method = None

    def __init__(self, champion_name_img_path, method=cv.TM_CCOEFF_NORMED):
        self.champion_name_img = cv.imread(champion_name_img_path, cv.IMREAD_COLOR)
        self.champion_name_img_w = self.champion_name_img.shape[1]
        self.champion_name_img_h = self.champion_name_img.shape[0]
        self.method = method

    def find(self, shop_img, threshold=0.5):

        result = cv.matchTemplate(self.champion_name_img, shop_img, self.method)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]),
                    self.champion_name_img_w, self.champion_name_img_h]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        return rectangles

    def get_click_points(self,rectangles):

        points = []
        for (x, y, w, h) in rectangles:
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            points.append((center_x, center_y))

        return points

    def draw_rectangles(self, shop, rectangles):

        line_color = (0,255,0)
        line_type = cv.LINE_4
        
        for(x,y,w,h) in rectangles:
            top_left = (x,y)
            bottom_right = (x+w,y+h)
            cv.rectangle(shop, top_left, bottom_right, line_color, lineType=line_type)
        return shop

    def draw_crosshairs(self, shop, points):

        marker_color = (255,0,255)
        marker_type = cv.MARKER_CROSS

        for (center_x,center_y) in points:
            cv.drawMarker(shop, (center_x, center_y), marker_color, marker_type)

        return shop
