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

range(10)  # Iterable

for i in range(5):
    print(i)

list(range(10))
range(0, 10, 2)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i, v in enumerate(a):
    print(i, v)


###### break, continue, else on loops #######

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    # When no break occurs
    else:
        print(n, 'is a prime number')


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

###### pass #######

# undefined from Haskell

class Foo:
    pass

def foo():
    pass

###### functions #######

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
    print()
    # Implicit return None

fib(2000)
f = fib
f(2000)
print(fib(0)) # None

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

###### default args #######
def ask_ok(a, b=4, c='Please try again!'):
    pass


i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# Wrong
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

# Ok
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

###### keywords args #######

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

###### Arbitrary Argument Lists #######

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

###### Unpacking Argument Lists #######

args = [3, 6]
list(range(*args))

###### Lambda #######

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

###### Documentation #######

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

###### Function Annotations #######

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
