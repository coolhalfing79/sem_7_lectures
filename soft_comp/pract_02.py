from ..ANN import Neuron
import numpy as np
neuron = Neuron(3, Neuron.arctan, 0)
neuron._inputs = np.random.random(size=3)
neuron._weights = np.random.random(size=3)
print(neuron.calc_out())