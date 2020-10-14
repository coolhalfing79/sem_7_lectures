'''
soft computing practical 6
'''
import numpy
from neuron import Neuron, bipolar_step


w = [1, -1, 0, 0.5]
C = 0.1
D = [-1, -1, 1]
X = numpy.array([[1, -2, 0, -1], [0, 1.5, -0.5, -1], [-1, 1, 0.5, -1]])

neuron = Neuron(activation_fn=bipolar_step, weights=w)

for epoch in range(5):
    print(f'\nepoch {epoch+1}')
    for x, di in zip(X, D):
        neuron.inputs = x
        o = neuron.calc_out()
        neuron.weights += C * (di- o) * x
        print(f'weights: {neuron.weights} f(net): {o} inputs: {neuron.inputs}')
