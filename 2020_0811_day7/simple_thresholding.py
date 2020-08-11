# thresholding : 이미지의 이진화
# 일반적으로 회색 음영 이미지를 0 or 255인 바이너리 이미지로 변환
# 픽셀값 p를 선택 -> p보다 작은 픽셀 모두 0으로 -> p보다 큰 픽셀은 255로 -> 이미지를 이진화
# 사용자가 thresholding 값 T를 정해줘야 함
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

# threshold 지정
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

cv2.imshow("Find Coins", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)