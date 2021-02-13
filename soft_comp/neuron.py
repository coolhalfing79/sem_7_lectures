'''
Introduction to activation functions and Implementation of an artificial neuron

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
        return self.act_fn(self.weights.T @ self.inputs + self.bias)

def signum(net):
    '''signum activation function'''
    return net >= 0

def bipolar_step(net):
    '''bipolar step activation function'''
    return 2 * int(net > 0) -1

# def softmax(net):
#     '''softmax activation function'''
#     return np.exp(net) / np.np.xp(net))

def u_peicewise_linear(net):
    '''unipolar peicewise linear activation function'''
    return min(1, max(0, net))

def b_peicewise_linear(net):
    '''bipolar peicewise linear activation function'''
    return min(1, max(-1, net))

def u_sigmoidal(net):
    '''unipolar sigmoidal activation function'''
    lam = 1
    return 1 / (1 + np.exp(-1 * lam * net))

def b_sigmoidal(net):
    '''bipolar sigmoidal activation function'''
    lam = 1
    return 2 / (1 + np.exp(-1 * lam * net)) - 1

def hyperbolic_tan(net):
    '''hyperolic tan activation function'''
    return np.tanh(net)

def arctan(net):
    '''arctan activation function'''
    return np.arctan(net)

def relu(net):
    '''relu activation function'''
    return max(0, net)

def leaky_relu(net):
    '''leaky relu activation function'''
    return max(0.01 * net, net)
