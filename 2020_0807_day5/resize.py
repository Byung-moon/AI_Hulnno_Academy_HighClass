# 이미지 크기 조정
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 150.0 / image.shape[1]  # 가로세로 비율 계산. 새로운 이미지 폭을 150픽셀로 정의
dim = (150, int(image.shape[0] * r)) # 이미지의 새로운 치수 계산. 새로운 이미지의 너비는 150픽셀

# 이미지 실제 크기 조정. cv2.resize(조정할 이미지, 새 이미지 치수, 보간법)
# 보간법 : 실제 이미지를 입력 값으로 조정하기 위한 알고리즘
# cv2 에서 크기 조정시 INT_AREA를 많이 사용하지만, cv2.INT_LINER, cv2.INT_CUBIC, cv2.INT_NEAREST도 사용
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

r = 50.0 / image.shape[0]   # 높이를 50픽셀로 설정
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)