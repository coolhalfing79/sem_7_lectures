'''
soft computing practical 6
'''
import numpy
from neuron import Neuron, b_sigmoidal


w = [1, -1, 0, 0.5]
C = 0.1
D = [-1, -1, 1]
X = numpy.array([[1, -2, 0, -1], [0, 1.5, -0.5, -1], [-1, 1, 0.5, -1]])
neuron = Neuron(activation_fn=b_sigmoidal, weights=w)

for x, di in zip(X, D):
    neuron.inputs = x
    o = neuron.calc_out()
    d_o = 0.5 *  (1 - o * o)
    neuron.weights += C * (di- o)* d_o * x
    print(neuron.weights)
