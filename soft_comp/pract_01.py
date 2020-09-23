import numpy as np
from hashlib import md5


#exe 1
data = 5649
atad = ''
while data > 0:
    atad += str(data%10)
    data = data//10
    
print(int(atad))

#exe 2
name = "Anirudha"
roll_no = 171104008
GATE_rank = 1
percentile = 99.99
print(f"name:{name} roll no:{roll_no} GATE rank:{GATE_rank} percentile:{percentile}")

#exe3
players = ['abc', 'de', 'ijk', 'efg', 'lmn', 'op', 'qq', 'rr']
for player in ['de', 'ijk', 'efg', 'op']:
    players.remove(player)
print(players)

#exe4
n = 6
for x in range(n):
	print(' ' * (n-x), end='')
	print('*', end='')
	if x ==3:
		print('******', end='')
	else:
		print(' ' * x * 2, end='')
	print('*')


#exe5
A1 = np.random.randn(5,4)
A2 = np.random.randn(3, 4)
A3 = np.concatenate((A1, A2))
A4 = np.concatenate((A3, np.random.randn(2, 4)))
A4 = np.concatenate((A4, np.random.randn(10, 6)), axis=1)
# print(A4.shape)
# print(A1.T, A2.T, A3.T, A4.T)

#exe6
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
	h = md5(x.encode()).hexdigest()
	name[x] = h
	num = input('mobile numbers:')
	hashdict[h] = num
print(name, hashdict)