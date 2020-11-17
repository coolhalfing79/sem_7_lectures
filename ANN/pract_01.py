'''
ANN practical 1
'''
# from pprint import pprint
import numpy
import matplotlib.pyplot as plt
from neuron import Neuron, b_sigmoidal

numpy.set_printoptions(precision=2)

W = [1, -1, 0, 0.5]
C = 0.1
D = [-1, -1, 1]
X = numpy.array([[1, -2, 0, -1], [0, 1.5, -0.5, -1], [-1, 1, 0.5, -1]])
weight_change = [W]
neuron = Neuron(activation_fn=b_sigmoidal, weights=W)

for epoch in range(250):
    if epoch < 5:
        print(f'\nepoch: {epoch + 1}')
    for x, di in zip(X, D):
        neuron.inputs = x
        o = neuron.calc_out()
        neuron.weights += C * (di- o) * 0.5 * (1 - o*o) * x
        if epoch <5 :
            print(f'weights: {neuron.weights}\tf(net): {o:.2f}')
    weight_change.append(list(neuron.weights))

# pprint(weight_change)

plt.title('change of weights in 250 epochs')
plt.plot(weight_change)
plt.legend(['w1', 'w2', 'w3', 'w4'])
plt.show()
