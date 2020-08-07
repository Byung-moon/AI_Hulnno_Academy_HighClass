# 이미지 변환
# 번역, 회전, 크기 조정, 플립, 자르기 등

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                 help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# [1, 0, 25] 에서 25는 이미지를 왼쪽 or 오른쪽으로 이동시킬 픽셀 수
# 양수는 오른쪽으로 음수는 왼쪽으로
# [0, 1, 50] 에서 50은 위아래로 이동시킬 픽셀수. 양수는 아래로, 음수는 위로 이동
M = np.float32([ [1, 0, 250], [0, 1, 500] ])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

M = np.float32([ [1, 0, -500], [0, 1, -900] ])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)