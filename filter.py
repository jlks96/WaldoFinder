import numpy as np 
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", help = "path to image")
args = vars(ap.parse_args())

image=cv2.imread(args["image"])