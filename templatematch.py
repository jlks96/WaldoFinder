import cv2
import numpy as np

img_rgb = cv2.imread('test.jpg')
img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('waldo.jpg', 0)