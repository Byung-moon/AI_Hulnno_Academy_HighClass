from matplotlib import pyplot as plt
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#image = cv2.imread(args["image"], 0)   # numpy를 이용한 히스토그램
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# 히스토그램 계산
# 그레이 스케일 이미지에는 하나의 채널만 있으므로 채널 = 0
# 마스크가 없으므로 None
# 256개의 저장소 사용
# 사용가능한 범위는 0~256
hist = cv2.calcHist(image, [0], None, [256], [0, 256])
#hist, bins = np.histogram(image.ravel(), 256, [0, 256])    # numpy를 이용한 히스토그램

plt.plot(hist)
plt.xlim([0, 256])
plt.show()