'''
design of an adaline
'''
import numpy as np


W = np.array([1, -1, 0, 0.5])
C = 0.1
D = [-1, -1, 1]
X = np.array([[1, -2, 0, -1], [0, 1.5, -0.5, -1], [-1, 1, 0.5, -1]])

for epoch in range(5):
    for x, d in zip(X, D):
        net = W.T @ x
        W += C * (d-net) * x
    print('epoch #', epoch, W)
