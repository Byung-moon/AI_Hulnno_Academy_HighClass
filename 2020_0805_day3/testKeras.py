import numpy as np
import keras

x_train = np.array( [0,1] )
y_train = x_train * 2 + 1
print(x_train)
print(y_train)
x_test = np.array([2,3])
y_test = x_test * 2 + 1
print(x_test)
print(y_test)


model = keras.models.Sequential()
print(type(model))

model.add(keras.layers.Dense(1, input_shape=(1,)))
model.summary()


