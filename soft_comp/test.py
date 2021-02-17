import numpy as np


I = np.array([0.5, 0.6, 0.1])
P = len(I)
W = np.ones((P, P))
for i, row in enumerate(W):
    for j, col in enumerate(row):
        if i == j:
            continue
        W[i, j] = -1/P
i = 0
while i < 5:
    I = np.maximum(0, W @ I)
    print(I)
    i += 1
