import numpy as np

def sign(net):
    return 2 * (net >= 0) -1

inputs = np.array([[ 1,  1,  1, -1],
                   [-1, -1, -1,  1],
                   [ 1,  1,  1,  1],
                   [ 1,  1, -1, -1],
                   [ 1, -1,  1, -1],
                   [-1,  1,  1, -1]])

W = np.array([[0, 1, 1, -1],
              [1, 0, 1, -1],
              [1, 1, 0, -1],
              [-1, -1, -1, 0]])

for o in inputs:
    print('\ninput:', o)
    # for epoch in range(5):
    o = sign(W @ o)
    print('output:', o)
