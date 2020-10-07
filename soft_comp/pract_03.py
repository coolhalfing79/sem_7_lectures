import neuron
import numpy


neuron = neuron.Neuron(neuron.arctan, numpy.random.random(size=3), 0)
neuron._inputs = numpy.random.random(size=3)
print(neuron.calc_out())
