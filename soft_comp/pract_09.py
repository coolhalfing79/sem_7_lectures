'''
simple competitive learning
'''
import numpy as np


X = np.array([[1.1, 1.7, 1.8],
              [0.0, 0.0, 0.0],
              [0.0, 0.5, 1.5],
              [1.0, 0.0, 0.0],
              [0.5, 0.5, 0.5],
              [1.0, 1.0, 1.0]])

W = np.array([[0.2, 0.7, 0.3],
              [0.1, 0.1, 0.9],
              [1.0, 1.0, 1.0]])
N = 0.5
#for epoch in range(5):
#print('\n###### epoch:', epoch+1, '######')
for x in X:
    d = []
    for w in W:
        tmp = x-w
        d.append(tmp.T @ tmp)
    i = np.argmin(d)
    W[i] += N * (x - W[i])
    print(W, '\n')
