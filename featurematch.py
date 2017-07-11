import numpy as np
import cv2
import matplotlib.pyplot as plt

template = cv2.imread('waldo.jpg', 0)
search = cv2.imread('test.jpg', 0)