#!/user/bin/env python3.7
# -*- coding: utf8 -*-

##### Lists #####

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()

##### Lists as Stacks #####

stack = [3, 4, 5]
stack.append(7)
stack.pop()

##### Lists as Queues #####

from collections import deque

# deque is a fast append queue.
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()

##### Lists comprehensions #####

squares = []
for x in range(10):
    squares.append(x**2)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3]
        for y in [3,1,4]
        if x != y]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# flatten a list
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]


# Transpose a Matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

# Alternative
list(zip(*matrix))


##### del #####

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]  # del all element
del a  # del object and pointer


##### Tuples and Sequences #####

# Tuples are immutable:
t = 12345, 54321, 'hello!'
t[0]  # WRONG: t[0] = 1
a, b, c = t

u = t, (1, 2, 3, 4, 5)
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])

empty = ()
singleton = 'hello',  # <-- note trailing comma
len(empty)
len(singleton)

##### Sets #####

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
'orange' in basket  # member
a = set('abracadabra')
b = set('alacazam')
a - b
a | b
a & b
a ^ b  # XOR

a = {x for x in 'abracadabra' if x not in 'abc'}

##### Dictionaries #####

s = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['jack']
del tel['sape']
tel['irv'] = 4127
list(tel)
sorted(tel)
'guido' in tel
'jack' not in tel

{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, guido=4127, jack=4098)

##### Looping #####

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.


##### Comparing Sequences, Tuples #####

(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C'
[[1,2,3],[4,5,6]] == [[1,2,3],[4,5,7]]
