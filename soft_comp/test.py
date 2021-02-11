import numpy as np


training_set = np.array([[1, 1, 1], [-1, -1, -1], [1, -1, -1]])
print(np.sum(training_set.T[0]* training_set.T[1]))
P=3
for i in range(P):
    for j in range(P):
        print(np.sum(training_set.T[i] * training_set.T[j])/P)
