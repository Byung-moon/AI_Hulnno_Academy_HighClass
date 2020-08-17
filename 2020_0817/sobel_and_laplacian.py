# 에지 검출은 픽셀 강도의 밝기가 분명하게 변화하는 이미지의 좌표를 찾기 위한
# 수학적 방법을 구현
# -> Canny enge detection
# -> Noise decreasing(Bluring)
# -> 이미지의 그래디언트(수평 및 수직 방향 모두에서 Sobel 커널 사용)
# -> 억제 및 히스테리시스 thresholding을 찾는 다단계 프로세스 적용
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 그레이 스케일로 변환
cv2.imshow("Original", image)

lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplacian", lap)
#cv2. waitKey(0)

# 64비트 부동소수점을 사용하는 이유 : 그래디언트 크기 이미지를 계산할 때
# 가장자리 특히 백색->흑색의 전환이 누락됨.
# uint8은 양수만 나타내기 떄문에 음의 기울기인 백색->흑색 을 표현x
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0) # 1,0으로 수직 모서리 찾기
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1) # 0,1로 수평 에지 찾기
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)