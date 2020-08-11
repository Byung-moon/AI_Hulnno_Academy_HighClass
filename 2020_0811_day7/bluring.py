# 블러링: 블러링을 하면
# 임계값 지정 및 가장자리 감지와 같은 이미지 처리 및 컴퓨터 비전에서
# 이미지가 더욱 매끄러워지면 성능이 향상됨
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

blurred = np.hstack([
    cv2.blur(image, (3,3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (30, 30))])
cv2.imshow("Averaged", blurred)
#cv2.waitKey(0)

# Gaussian Bluring -> 중앙 픽셀에 인접한 픽셀에 더 많은 가중치를 부여
# --> 보다 더 자연스러운 블러링 연출
blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian", blurred)
#cv2.waitKey(0)

# median bluring -> 소금 후추 노이즈를 제거할 때 가장 효과적
# 커널 크기 k를 정함 -> k x k 의 이웃 픽셀 고려
# 일반적인 방법과 달리 중앙 픽셀을 이웃의 평균값으로 바꾸고
# 중앙 픽셀을 이웃의 중앙값으로 대체
blurred = np.hstack([
    cv2.medianBlur(image, 3),   # 기본적으로 하나의 커널값 k만 주면 k x k 로 적용되어 사용
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

# bilateral bluring
# 가장자리를 유지하면서 노이즈를 줄이기 --> 두 개의 가우시안 분포를 도입
# 첫번째 가우시안 : 가깝게 나타나는 픽셀만 고려
# 두번째 가우시안 : 인접한 픽셀 강도를 모델링 -> 유사한 강도를 가진 픽셀만 실제 계산에 포함
# 단점 : 다른 블러링보다 느림
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Biateral", blurred)
cv2.waitKey(0)