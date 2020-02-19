#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

###### Numbers #######

17 // 3  # floor division, discards the fractional part
2 ** 5   # powder

###### Strings #######

# '\' prevents end-of-line
print("""\
Usage: xxx
    - h halp         Display halp
""")

3 * 'jo' + 'nya'
'Please' 'dont'  # this is valid

word = 'Python'
word[0]  # first character
word[-1]  # last character
word[0:2]  # 'Py'
word[2:5]  # 'tho'
word[:2]  # 'Py'
word[2:]  # 'thon'
word[2:100]  # 'thon'
len(word)

###### Lists #######
squares = [1, 4, 9, 16, 25]
squares[0]
squares[2:]
squares[:]  # Shallow copy
squares + [36, 49]

cubes = []
cubes = [1, 8, 27, 65, 125]
cubes[3] = 3 ** 4
cubes.append(216)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']

matrix = [[1, 2, 3], [4, 5, 6]]
matrix[0][0]  # 1
