# adaptive thresholding : 픽셀의 작은 이웃을 고려하여 최적의 T 값을 찾는 방법
# 픽셀 강도의 범위가 극적일때,
# T의 최적값이 이미지의 다른 부분에 따라 달라질 수 있는 경우 사용
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image to Gray", image)

# 현재 픽셀 인접 영역에 대한 thresholding을 계산하는 Google의 방법
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", thresh)

# 가우시안(가중 평균) thersholding을 적용
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)