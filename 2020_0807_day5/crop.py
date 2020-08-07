# 이미지 자르기

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# y축 600부터 1300까지, x축 700부터 1200까지
cropped = image[600:1300, 700:1200]
cv2.imshow("Romantic Couple", cropped)
cv2.waitKey(0)