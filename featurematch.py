
import numpy as np
import cv2
import matplotlib.pyplot as plt


# Our detector
orb = cv2.ORB()

kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(search, None)

# Hamming is used to determine distance

bruteforce = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

match = bruteforce.match(des1, des2)


match = sorted(match, key = lambda x: x.distance)
