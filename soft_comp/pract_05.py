from Neuron import Neuron
from Neuron import bipolar_step 
import numpy

weights = [1, -1, 0, 0.5]

inputs = [[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]]
c = 1

neuron = Neuron(activation_fn=bipolar_step, weights=weights, bias=0)
for epoch in range(5):
    print(f'epoch {epoch+1}')
    for x in inputs:
        neuron._inputs = numpy.array(x)
        o = neuron.calc_out()
        neuron._weights += c * o * neuron._inputs
        print(f'weights: {neuron._weights}\t\tf(net): {o}\tinputs: {neuron._inputs}')
    print()
