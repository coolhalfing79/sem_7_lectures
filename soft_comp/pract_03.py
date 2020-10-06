import Neuron
import numpy


neuron = Neuron.Neuron(Neuron.arctan, nnumpy.random.random(size=3), 0)
neuron._inputs = numpy.random.random(size=3)
print(neuron.calc_out())
