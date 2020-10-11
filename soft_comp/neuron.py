'''
defines a neuron class for use in the following practicals
'''
import numpy as np


class Neuron: # pylint: disable=too-few-public-methods
    '''McCulloch pitts neuron model'''
    def __init__(self,activation_fn, weights, bias=0):
        self.weights = np.array(weights)
        self.inputs = np.empty_like(self.weights)
        self.act_fn = activation_fn
        self.bias = bias

    def calc_out(self):
        '''calculates neuron output using specified activation function'''
        return self.act_fn(self.weights * self.inputs + self.bias)

def signum(w_x):
    '''signum activation function'''
    return sum(w_x) >= 0

def bipolar_step(w_x):
    '''bipolar step activation function'''
    return 2 * int(sum(w_x) > 0) -1

def softmax(w_x):
    '''softmax activation function'''
    return np.exp(w_x) / np.sum(np.exp(w_x))

def u_peicewise_linear(w_x):
    '''unipolar peicewise linear activation function'''
    return min(1, max(0, sum(w_x)))

def b_peicewise_linear(w_x):
    '''bipolar peicewise linear activation function'''
    return min(1, max(-1, sum(w_x)))

def u_sigmoidal(w_x):
    '''unipolar sigmoidal activation function'''
    lam = 1
    return 1 / (1 + np.exp(-1 * lam * np.sum(w_x)))

def b_sigmoidal(w_x):
    '''bipolar sigmoidal activation function'''
    lam = 1
    return 2 / (1 + np.exp(-1 * lam * np.sum(w_x))) - 1

def hyperbolic_tan(w_x):
    '''hyperolic tan activation function'''
    return np.tanh(w_x)

def arctan(w_x):
    '''arctan activation function'''
    return np.arctan(w_x)

def relu(w_x):
    '''relu activation function'''
    max(0, np.sum(w_x))

def leaky_relu(w_x):
    '''leaky relu activation function'''
    net = np.sum(w_x)
    max(0.01 * net, net)
