#!/user/bin/env python3.7
# -*- coding: utf8 -*-

# Built-in Exceptions: https://docs.python.org/3.7/library/exceptions.html#bltin-exceptions



# while True:
    # try:
        # x = int(input("Please enter a number: "))
        # break
    # except ValueError:
        # print("Oops! That was not a valid number. Try again...")


# This is very similar to Java.
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except B:
        print("B or subtype")


import sys

try:
    f = open('peace.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# else is executed if the try does not raise an exception
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

#### User-defined Exceptions ####

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


#### Defining Clean-up Actions ####

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# Use with for clean-up files
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
