# 픽셀에 접근하고 조작하는 코드
# OpenCV는 RGB 채널을 역순으로 저장. ** 중요 **
# 하나의 창에서 image를 두 번 띄울 순 없음

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

# Original 이라는 title을 갖고 image 출력
# image가 계속 떠 있을 수 있게 유지
cv2.imshow("Original", image)
cv2.waitKey(0)

# 이미지의 왼쪽 상단 모서리. 즉, 좌표 (0,0)을 잡아 픽셀값을 저장. 픽셀의 데이터 타임은 튜플
# 각 채널의 값을 콘솔로 출력
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# 이미지의 (x,x) 픽셀이 (0, 0, 255)-빨강 의 값을 갖게 조작
for x in range(50,900):
    image[x, x] = (0, 0, 255)

# (b, r, g) 에 바뀐 픽셀값 대입
(b, g, r) = image[0, 0]

# 바뀐 픽셀 값 출력
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b)) # 바뀐 픽셀 값 출력

# 이미지의 100 x 100 픽셀 영역 설정. 왼쪽 상단 코너를 의미
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

# (0,0) 픽셀이 빨간색으로 바뀐 이미지를 출력
#cv2.imshow("Fixed (0,0) to Red", image)

# 코너가 초록색으로 바뀐 이미지 출력
cv2.imshow("Updated", image)
cv2.waitKey(0)