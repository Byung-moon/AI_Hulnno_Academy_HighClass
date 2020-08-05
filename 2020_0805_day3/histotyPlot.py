
import keras
import numpy as np
import matplotlib.pyplot as plt


# 트레이닝 데이터 설정
x_train = np.array([0,1])
y_train = x_train * 2 + 1

# 트레이닝 값 출력
print(x_train)
print(y_train)

# 테스트 값 설정
x_test = np.array([2,3])
y_test = x_test * 2 + 1

# 테스트 값 출력
print(x_test)
print(y_test)

# x, h, y 설정
x = keras.layers.Input(shape=(1,))
h = keras.layers.Dense(2)(x)
y = keras.layers.Dense(1)(h)

# x, y를 바탕으로 모델 생성
model = keras.models.Model(x,y)

# 모델 개요 출력
model.summary()

# 모델 컴파일 후 학습 결과를 history에 저장
model.compile('SGD', 'mse')
history = model.fit(x_train, y_train, epochs=1000, verbose = 0)

# 그래프 그리기
plt.plot(history.history['loss'])
plt.title('Loss')

# 그래프 출력
plt.show()