import numpy as np

def sign(net):
    return 2 * (net >= 0) -1

X = np.array([
    [ 1,  1,  1, -1],
    [-1, -1, -1,  1],
    [ 1,  1,  1,  1],
    [ 1,  1, -1, -1],
    [ 1, -1,  1, -1],
    [-1,  1,  1, -1]
])

n = len(X[0])
P = len(X)
W = np.zeros((n, n))

def sign(net):
    return 2 * (net > 0) -1

for i in range(n):
    for j in range(n):
        W[i, j] = np.sum(X[:, i] * X[:, j]) / P

I = np.random.uniform(-1, 1, (10, 4))
print('stored vectors:\n', X)
for i in I:
    print('\ninput:', i)
    o = i
    while o not in X:
        o = sign(W @ o)
    print('output:', o)
