'''
soft computing practical 5
'''
import numpy
from neuron import Neuron, bipolar_step

weights = [1, -1, 0, 0.5]

inputs = [[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]]
C = 1

neuron = Neuron(activation_fn=bipolar_step, weights=weights)
for epoch in range(5):
    print(f'\nepoch {epoch+1}')
    for x in inputs:
        neuron._inputs = numpy.array(x)
        o = neuron.calc_out()
        neuron._weights += C * o * neuron._inputs
        print(f'weights: {neuron._weights} f(net): {o} inputs: {neuron._inputs}')
