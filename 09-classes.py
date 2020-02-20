#!/user/bin/env python3.7
# -*- coding: utf8 -*-

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = [1, 2, 3, 4]

    # Class method
    def f(self):
        return 'hello world'

x = MyClass()
print(x.data)
# The follwing is valid ...
x.f = 1
print(x.f) # 1

# class instantiation automatically invokes __init__()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

class Foo:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Foo(3.0, -4.5)
x.r, x.i

# Data attributes .. don't

x.counter = 1  # It's created the first time is assigned.
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

class Dog:
    # Shared between all instances.
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = [] # Local to the instance

    def add_trick(self, trick):
        self.tricks.append(trick)



##### Inheritance #####

class Animal:
    def f(self):
        print("ff")

    def feed(self):
        print('nyum')

class Dog(Animal):
    def feed(self):
        super().feed()

x = Dog()
x.f()
x.feed()

p = isinstance(x, Dog)
p = issubclass(Dog, Animal)
print(f"Is Dog subclass of Animal: {p}")
p = issubclass(Animal, Dog)
print(f"Is Animal subclass of Dog: {p}")

class A:
    def a(self):
        print('a')

    def diamond(self):
        print("from A")

class B:
    def b(self):
        print('b')

    def diamond(self):
        print("from B")

class C(A, B):
    def c(self):
        super().a()
        super().b()
        print('c')

    # Diamond dependencies are resolved by
    # calling the super().x from left-to-right.
    def diamond(self):
        super().diamond()

c = C()
c.c()
c.diamond()

#### Private Variables ####

# No private instances.

# Convention: use _foo

# Name mangling: prevents accidental calls to overrided methods
#                do not use it as private.

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)



#### Iterators ####

# iter(), next()

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("./lore.txt"):
    print(line, end='')


s = 'abc'
it = iter(s)
print(next(it))
print(next(it))


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('ABCDE')
for char in rev:
    print(char)


#### Generators ####

# __iter__() and __next__() are created automatically by yield.
def reverse(xs):
    for i in range(len(xs)-1, -1, -1):
        yield xs[i]

for char in reverse('golf'):
    print(char)


#### Generator Expressions ####

sum(i*i for i in range(10))


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

unique_words = set(word for line in page for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
