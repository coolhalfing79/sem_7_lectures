'''
roulette wheel selection
'''

import numpy as np
import random
from pprint import pp

# initialise population
int1 = np.random.rand(10) * 10
int2 = np.random.rand(10) * 10
population = [(a, b) for a, b in zip(int1, int2)]

# goal of genetic algorithm is to maximise a*b
# fitness can be simply a*b
def fit(individual):
    a, b = individual
    return a * b

def rws(population):
    s = 0
    T = 0
    for individual in population:
        T += fit(individual)
    r = random.uniform(0, T)
    for individual in population:
        # visual representation of roulette wheel selection
        fitness_percent = int(fit(individual)/T * 100)
        print('█' * (fitness_percent-1)+'▉', end='') #██▉▉█
    print('\n'+' ' * int(r/T * 100)+'⮝')

    for p in population:
        s += fit(p)
        if s > r:
            return p

selected = rws(population)
print('phenotype:', selected)
print('fitness:', fit(selected))
