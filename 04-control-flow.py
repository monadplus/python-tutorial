#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

###### If #######
x = 5  # int(input("Please enter an integer:"))
if x < 0:
    print("Negative integer")
elif x == 0:
    print("Zero")
else:
    print("Positive integer")

###### for #######
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:  # Loops over a copy
    if len(w) > 6:
        words.insert(0, w)
print(words)

###### range #######
range(10)

for i in range(5):
    print(i)

list(range(10))
range(0,10,2)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
