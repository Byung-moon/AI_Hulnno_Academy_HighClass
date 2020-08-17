# Canny Edge Detector
# : 다단계 프로세스.
# 노이즈를 제거하고 x 및 y 방향으로 Sobel 그래디언트 이미지를 계산하고
# 가장자리를 억제하고 최종적으로 픽셀이 "가장자리 모양"인지 아닌지를 결정하는
# 히스테리시스 thresholding 단계를 계산하는 Bluring 처리가 포함
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# edge detection 이전에 Bluring 하면
# 이미지에서 노이즈가 아닌 노이즈가 있는 가장자리를 제거하는데 도움
image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow("Blured", image)

canny = cv2.Canny(image, 30, 150)

cv2.imshow("Canny", canny)
cv2.waitKey(0)