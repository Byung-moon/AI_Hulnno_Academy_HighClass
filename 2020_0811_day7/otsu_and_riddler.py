# otsu and riddler-calvard
# otsu를 사용하여 T의 값을 자동으로 계산
# Otsu의 방법 :
# 1. 이미지의 그레이 스케일 히스토그램에 두 개의 피크가 있다고 가정
# 2. 두 피크를 분리하는 최적 값 찾기
# --> OpenCV는 Otsu의 방법을 지원하지만 Luis Pedro Coelho 가 구현한 것이 더 Pythonic함
from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 그레이로 이미지 전처리
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 블러 처리
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}", format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

T = mahotas.thresholding.rc(blurred)
print("Riddler-CalvardL {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)