'''
brain state in a box
'''
import numpy as np


training_set = np.array([[1, 1, 1], [-1, -1, -1], [1, -1, -1]])
P = len(training_set)
W = np.empty_like(training_set, dtype=float)
I = np.array([0.5, 0.6, 0.1])

def ramp(x):
    return np.maximum(-1, np.minimum(1, x))

for i in range(P):
    for j in range(P):
        W[i][j] = np.sum(training_set[:, i] * training_set[:, j]) / P
        
print('weights:\n', W)
print('\ncorrupted input:\n', I)

while(I not in training_set):
    I = ramp(W.T @ I)
    
print('\ncorrected input:\n', I)
