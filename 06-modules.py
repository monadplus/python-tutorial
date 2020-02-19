#!/user/bin/env python3.7
# -*- coding: utf8 -*-

import fibo

# Global variable
print(fibo.__name__)

fibo.fib(1000)
print(fibo.fib2(100))

from fibo import fib, fib2
fib(1000)

from fibo import *

import fibo as fib
fib.fib(1000)

from fibo import fib as fibonacci
fibonacci(1000)


##### Module Search Path #####

# Search modules in sys.path which is initialized in:
#
# * the directory containing the input script (symlinks are follwed)
# * PYTHONPATH
# * the installation-dependent default
#
# Programs can modify sys.path
import sys
print(sys.path)
sys.path.append('/usr/bin')


#### "Compiled" Python files #####

# To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc
#
# Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.
#
# A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that’s faster about .pyc files is the speed with which they are loaded.

#### Standard Modules #####

# Python interpreter comes with some standard modules.

# Some grant access to operating system primitives such as system calls.

print(fibo)  # names defined at module
print(dir())  # which names are defined so far

#### Packages ####

import example.foo
example.foo.surprise()

from example import foo
foo.surprise()

from example.foo import surprise
surprise()

from example.nested import foo
foo.surprise2()

# The __init__.py files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path.


##### Importing * From a Package ######

# What happens when the user writes:
from example import *

# if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered.
#
# If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace
faa.surprise3


#### Intra-package References ####

# Supose you are in a subpackage.
#
# * Absolute path work
# * Relative path work
#
# Example:
# from . import echo
# from .. import formats
# from ..filters import equalizer


#### __path__ ####


# Packages supports the attribute __path__.

print(example.__path__)  # name of the directory containing the __init__.py
