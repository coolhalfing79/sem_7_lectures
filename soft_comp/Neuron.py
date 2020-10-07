import numpy as np
import matplotlib.pyplot as plt
import math


class Neuron:
    def __init__(self,activation_fn, weights, bias):
        self._weights = np.array(weights)
        self._inputs = np.empty_like(self._weights)
        self.act_fn = activation_fn
        self.bias = bias

    def calc_out(self):
        return self.act_fn(self._weights * self._inputs + self.bias)


def signum(wx):
    return sum(wx) >= 0

def bipolar_step(wx):
    return 2 * int(sum(wx) > 0) -1

def softmax(wx):
    return np.exp(wx) / np.sum(np.exp(wx))

def u_peicewise_linear(wx):
    return min(1, max(0, sum(wx)))

def b_peicewise_linear(wx):
    return min(1, max(-1, sum(wx)))

def u_sigmoidal(wx):
    l = 1
    return 1 / (1 + math.exp(-1 * l * np.sum(wx)))

def b_sigmoidal(wx):
    l = 1
    return 2 / (1 + math.exp(-1 * l * np.sum(wx))) - 1

def hyperbolic_tan(wx):
    return np.tanh(wx)

def arctan(wx):
    return np.arctan(wx)

def relu(wx):
    max(0, np.sum(wx))

def leaky_relu(wx):
    s = np.sum(wx)
    max(0.01 * s, s)
