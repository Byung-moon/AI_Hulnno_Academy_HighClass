import keras
import numpy as np

# keras Sequential 모델
model = keras.models.Sequential()
print(type(model))

model.add(keras.layers.Dense(1, input_shape=(1,)))
model.summary()

x_test = np.array([2,3])
y_test = x_test * 2 + 1

x_train = np.array( [0,1] )
y_train = x_train * 2 + 1

y_predict = model.predict(x_test)
print(y_predict.flatten())
print(y_test)

# 모델 컴파일
# 첫번째 인자는 optimizer. 즉, 최적화 방법을 'SGD'를 사용,
# 두번째 값은 예측값과 실제 원하는 값의 차이를 정하는 loss fuction
model.compile('SGD', 'mse')

# fit 함수를 사용하여 weight 값들을 학습.
# 첫번째 인자는 학습 데이터의 그룹, 두번째는 출력 학습 데이터의 그룹.
# epoch는 전체 학습데이터를 몇 번 반복해서 학습시킬지
# verbose=0 은 학습하는 동안 중간에 log를 출력 x
model.fit(x_train, y_train, epochs=1000, verbose=0)

# 다시 테스트 데이터를 사용하여 모델이 예측한 데이터와 실제 데이터 비교.
# 학습 전보다 예측값과 실제 값이 비슷해짐
y_predict = model.predict(x_test)
print(y_predict.flatten())
print(y_test)
