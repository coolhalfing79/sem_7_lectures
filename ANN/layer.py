"""
layer
"""
import numpy as np


def b_sigmoidal(w_x):
    '''bipolar sigmoidal activation function'''
    lam = 1
    return 2 / (1 + np.exp(-1 * lam * w_x)) - 1


class Layer:
    """
    creates a layer of neurons
    """
    def __init__(self, weights, inputs):
        self.weights = np.array(weights)
        self.inputs = np.array(inputs)

    def forward(self):
        '''layer output'''
        return b_sigmoidal(self.weights @ self.inputs)


if __name__ == "__main__":
    V = [[1, -2, 3],
         [2, 0, -1]]
    W = np.array([[1, 0, 2],
        [1, -2, 3]])
    X = np.array([1, 3, -1])
    D = [0.95, 0.05]
    C = 1
    df = lambda x: 0.5 * (1 - x * x)

    l1 = Layer(V, X)
    Y = l1.forward()
    dfj = df(Y)
    print('Oj:', Y)
    Y = np.concatenate((Y, np.array(-1)), axis=None)
    l2 = Layer(W, Y)
    O = l2.forward()
    print('Ok:', O)
    dfk = df(O)
    print(D, O, dfj, dfk, W)
    deltaV = C * dfj[0] * X * (((D-O) * dfk[0]) @ W[:, :1])
    print(deltaV)

if False:
    while True:
        print('impossible')
