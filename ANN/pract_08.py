'''
pocket algorithm
'''
import numpy as np


w = np.array([1, -1, 0, 0.5])
C = 0.1
D = [-1, -1, 1]
X = np.array([
    [ 1.0, -2.0,  0.0, -1.0],
    [ 0.0,  1.5, -0.5, -1.0],
    [-1.0,  1.0,  0.5, -1.0]
])

pocket = w
run_length = 0
best_run_length = 0

def f(net):
    return 2 * (net > 0) -1

for epoch in range(5):
    print('\nepoch #', epoch+1)
    for x, d in zip(X, D):
        r = d - f(w.T @ x)
        if r == 0:
            run_length += 1
        if r != 0:
            if run_length > best_run_length:
                best_run_length = run_length
                pocket = w.copy()
            w += C * r * x
            run_length = 0
        print(w,'run length:', run_length)
    print('pocket:', pocket)
for x, d in zip(X, D):
    print(f'\ninput: {x} f(net)={f(w.T @ x)} d={d}')
