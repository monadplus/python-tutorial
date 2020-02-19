#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

# utf8 is the implicit default.

"""
$ python -c 'import os; print(f"Current dir: {os.getcwd()}")'

$ python -i -m 'module' [arg] ... # executes the module in interactive mode
"""

import sys


# $ python 02-python-interpreter.py 1 "hi" 123
# Arguments: ['02-python-interpreter.py', '1', 'hi', '123']
args = sys.argv  # regular list
print(f"Arguments: {args}")
print(args[0])
