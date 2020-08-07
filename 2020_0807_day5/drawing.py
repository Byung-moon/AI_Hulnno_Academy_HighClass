import numpy as np
import cv2

# 이미지 초기화. np.zeros 를 이용하여 300x300 픽셀 이미지 생성.
canvas = np.zeros((300, 300, 3), dtype = "uint8")

#빨간색, 녹색, 파란색 각각 1개씩 3개의 채널에 대해 공간 할당. 각각의 색에 대한 튜플 정의.
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)

# (0,0) 부터 (300, 300) 까지 선을 그림. 색은 green 값.
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# (300,0) 부터 (0, 300) 까지 선을 그림. 색은 red값, 두께는 3픽셀로 설정
cv2.line(canvas, (300,0), (0,300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# (10, 10)부터 (60, 60)까지 사각형을 그림.
cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 빨간색 사각형 그리기
cv2.rectangle(canvas, (50,200), (200,255), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 파란색 사각형 그리기. -1을 두께로 설정하면 꽉 찬 사각형
cv2.rectangle(canvas, (200,50), (255,125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 원 그리기
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

# 흰색 튜플 설정
white = (255, 255, 255)

# (centerX, centerY)를 중심으로 25 픽셀 간격마다 흰색 원을 그림.
# circle 함수의 r 값은 반지름을 의미.
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# 무작위로 원 25개 그리기
for i in range(0, 25):
        radius = np.random.randint(5, high = 20)   # 반지름을 랜덤으로
        color = np.random.randint(0, high = 256, size = (3,)).tolist()  # 색상을 랜덤으로. 3개의 값을 갖는 랜덤 튜플. 최댓값은 256
        pt = np.random.randint(0, high = 300, size=(2,))    # 원의 중심을 (x,y)의 랜덤 튜플로 저장
        cv2.circle(canvas, tuple(pt), radius, color, -1)    # 원 그리기

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

