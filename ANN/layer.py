"""
dense layer
"""
import numpy as np
from neuron import Neuron, b_sigmoidal

class Layer:
    """
    creates a layer of neurons
    """
    def __init__(self, weights, inputs_array):
        self.neurons = [Neuron(activation_fn=b_sigmoidal, weights=weight) for weight in weights]
        for neuron in self.neurons:
            neuron.inputs = inputs_array

    def forward(self):
        '''layer output'''
        return [neuron.calc_out() for neuron in self.neurons]

if __name__ == "__main__":
    V = [[1, -2, 3],
         [2, 0, -1]]
    W = [[1, 0, 2],
        [1, -2, 3]]
    X = np.array([1, 3, -1])

    l1 = Layer(V, X)
    Y = l1.forward()
    print('Oj:', Y)
    Y.append(-1)
    l2 = Layer(W, Y)
    print('Ok:', l2.forward())