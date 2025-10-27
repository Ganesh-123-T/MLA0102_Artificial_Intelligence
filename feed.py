import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(1)
w1 = 2 * np.random.random((2, 3)) - 1
w2 = 2 * np.random.random((3, 1)) - 1

for i in range(10000):
    l1 = X
    l2 = sigmoid(np.dot(l1, w1))
    l3 = sigmoid(np.dot(l2, w2))
    l3_error = y - l3
    l3_delta = l3_error * sigmoid_derivative(l3)
    l2_error = l3_delta.dot(w2.T)
    l2_delta = l2_error * sigmoid_derivative(l2)
    w2 += l2.T.dot(l3_delta)
    w1 += l1.T.dot(l2_delta)

print("Final Output after training:")
print(l3)
