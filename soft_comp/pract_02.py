import Neuron
import numpy


neuron = Neuron.Neuron(3, Neuron.arctan, 0)
neuron._inputs = numpy.random.random(size=3)
neuron._weights = numpy.random.random(size=3)
print(neuron.calc_out())