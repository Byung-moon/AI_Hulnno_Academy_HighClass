import keras
import numpy as np

x_train = np.array([0, 1])
y_train = x_train * 2 + 1

print(x_train)
print(y_train)

x_test = np.array([2, 3])
y_test = x_test * 2 + 1

print(x_test)
print(y_test)

# 입력을 받는 입력 layer 만듦
# 입력 데이터의 모양을 알려주기 위해 shape 지정
x = keras.layers.Input(shape=(1,))
print(type(x))

# 이전 layer의 유닛과 모두 연결되는 Dense layer 만듦
# 유닛의 개수는 1
# 전의 layer. 즉, 입력 layer와 연결되지 않은 상태
d = keras.layers.Dense(1)
print(type(d))

y = d(x)
print(type(d))
print(type(y))

# 입력과 출력을 지정하여 Model 생성. 첫 번째 인자 : 입력, 두번째 : 출력
model = keras.models.Model(x,y)

# 모델 개요 출력
model.summary()

# 학습 전의 예측값 출력
y_predict = model.predict( x_test )
print( y_predict.flatten() )
print( y_test )


# compile 후 학습을 준비하고 fit을 사용하여 모델을 학습
model.compile('SGD', 'mse')
model.fit(x_train, y_train, epochs=1000, verbose=0)

# Functional 모델을 사용하여 학습한 결과 출력
# flatten() : data를 1차원으로 만들어줌
y_predict = model.predict(x_test)
print(y_predict.flatten())
print(y_test)
