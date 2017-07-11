import numpy as np
import cv2
import matplotlib.pyplot as plt

# Loaded the images
# Template is the picture that we are trying to find
# Search is the image we are looking in

template = cv2.imread('waldo.jpg', 0)
search = cv2.imread('test.jpg', 0)

# Our detector
orb = cv2.ORB()

kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(search, None)

# Hamming is used to determine distance

bruteforce = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

match = bruteforce.match(des1, des2)


match = sorted(match, key = lambda x: x.distance)


result = cv2.drawMatches(template,kp1, search,kp2, matches[:100], flags =3)

plt.imshow(result), plt.show()
