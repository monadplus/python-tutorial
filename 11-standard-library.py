#!/user/bin/env python3.7
# -*- coding: utf8 -*-

#### Output Formatting

# abbreviated displays
import reprlib
reprlib.repr('supercalifragilisticexpialidocious')
reprlib.repr(set('supercalifragilisticexpialidocious'))


import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30)


import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

import locale
locale.setlocale(locale.LC_ALL)

conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)
locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True)


#### Templating ####


from string import Template
t = Template('${village} folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# t.substitute(d) # Fails if a key is missing
t.safe_substitute(d)


#### Working with Binary Data Record Layouts ####

# import struct

# with open('lore.zip', 'rb') as f:
    # data = f.read()

# start = 0
# for i in range(3):                      # show the first 3 file headers
    # start += 14
    # fields = struct.unpack('<IIIHH', data[start:start+16])
    # crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    # start += 16
    # filename = data[start:start+filenamesize]
    # start += filenamesize
    # extra = data[start:start+extra_size]
    # print(filename, hex(crc32), comp_size, uncomp_size)

    # start += extra_size + comp_size     # skip to the next header

#### Multi-threading ####

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('lore.txt', 'lore2.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')


#### Logging ####

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')



#### Weak References ####

# Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.


# This approach works fine for most applications but occasionally there is a need to track objects only as long as they are being used by something else. Unfortunately, just tracking them creates a reference that makes them permanent. The weakref module provides tools for tracking objects without creating a reference.


import weakref, gc

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']

del a
gc.collect()

# d['primary']                # entry was automatically removed



#### Working with Lists ####

# Homogeneous fast list
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
a[1:3]

# For queues, breadth first tree searches, ...
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)

# Sorted Lists
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores

# Heaps
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries



#### Decimal Floating Point Arithmetic ####

"""
The decimal module offers a Decimal datatype for decimal floating point arithmetic. Compared to the built-in float implementation of binary floating point, the class is especially helpful for

    * financial applications and other uses which require exact decimal representation,

    * control over precision,

    * control over rounding to meet legal or regulatory requirements,

    * tracking of significant decimal places, or

    * applications where the user expects the results to match calculations done by hand.
"""

from decimal import *

round(Decimal('0.70') * Decimal('1.05'), 2) # 0.74
round(.70 * 1.05, 2) # 0.73




Decimal('1.00') % Decimal('.10') # 0.00
1.00 % 0.10                      # 0.09999999999999..

sum([Decimal('0.1')]*10) == Decimal('1.0') # True
sum([0.1]*10) == 1.0                       # False


getcontext().prec = 36
Decimal(1) / Decimal(7)
