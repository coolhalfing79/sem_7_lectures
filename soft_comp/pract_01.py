'''
Introduction to python
'''
from pprint import pprint
from hashlib import md5
import numpy as np


np.set_printoptions(precision=2)
#exe 1
DATA = 5649
ATAD = ''
while DATA > 0:
    ATAD += str(DATA%10)
    DATA = DATA//10

print('exe 1\n', int(ATAD))

#exe 2
NAME = "Anirudha"
ROLL_NO = 171104008
GATE_RANK = 1
PERCENTILE = 99.99
print('exe 2\n'+ f"name:{NAME} roll no:{ROLL_NO} GATE rank:{GATE_RANK} percentile:{PERCENTILE}")

#exe3
players = ['abc', 'de', 'ijk', 'efg', 'lmn', 'op', 'qq', 'rr']
for player in ['de', 'ijk', 'efg', 'op']:
    players.remove(player)
print('exe 3\n', players)

#exe4
print('exe 4')
N = 6
for x in range(N):
    print(' ' * (N-x), end='')
    print('*', end='')
    if x ==3:
        print('******', end='')
    else:
        print(' ' * x * 2, end='')
    print('*')


#exe5
print('exe 5')
print('random arrays')
A1 = np.random.randn(5,4)
A2 = np.random.randn(3, 4)
print('A1:\n', A1, '\nA2:\n', A2, '\nthe two arrays joined together')
A3 = np.concatenate((A1, A2))
print('A3:\n', A3)
A4 = np.concatenate((A3, np.random.randn(2, 4)))
A4 = np.concatenate((A4, np.random.randn(10, 6)), axis=1)
print('A4:\n', A4, '\nshape of new array', A4.shape)
print('\nA1.T\n', A1.T, '\nA2.T\n', A2.T,'\nA3.T\n', A3.T,'\nA4.T\n', A4.T)

#exe6
print('exe 6')
naava = ['Anirudha', 'Bnirudha', 'Cnirudha', 'Dnirudha', 'Enirudha']
numbers = [1234567890, 2345678901, 3456789012, 4567890123, 5678901234]
name = {naav:md5(naav.encode()).hexdigest() for naav in naava}
hashdict  = dict(zip(name.values(), numbers))
for x in range(2):
    x = input('names to delete:')
    hashval = name[x]
    del name[x]
    del hashdict[hashval]
for x in range(2):
    x = input('name to add:')
    H = md5(x.encode()).hexdigest()
    name[x] = H
    num = input('mobile numbers:')
    hashdict[H] = num
pprint(name)
pprint(hashdict)
