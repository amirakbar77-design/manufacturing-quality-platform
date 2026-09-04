# 1 = scalar [1,] = vector [n,] = matrix [n,m] = tensor [n,m,p]
# y = wx + b/// w = learned weights, x = input, b = learned bias/// y = output
# core calculation used by many machine-learning models to turn input features into an output.


import numpy as np

x = [300, 40, 100]
w = [0.2, 0.6, 0.1]
b = 5

dot_product = x[0] * w[0] + x[1] * w[1] + x[2] * w[2] + b
print(dot_product)

dot_product_2 = [x[i] * w[i] for i in range(len(x))]
print(sum(dot_product_2) + b)

dot_product_3 = 0
for i in range(len(x)):
    dot_product_3 += x[i] * w[i]
print(dot_product_3 + b)

y = np.dot(x, w) + b
print(y)

sensor_values = [42, 55, 68]
weights = [0.2, 0.5, 0.3]
bias = 4

dot_product_4 = 0

for i in range(len(sensor_values)):
    dot_product_4 += sensor_values[i] * weights[i]
print(dot_product_4 + bias)
