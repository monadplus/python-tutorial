#!/user/bin/env python3.7
# -*- coding: utf8 -*-

#### OS interface ####

import os

current_dir = os.getcwd()
os.chdir('/etc/nixos')
os.chdir(current_dir)
print(os.system('ls'))

#dir(os)  # All module functions
#help(os) # extensive manual page

import shutil

shutil.copyfile('./foo.json', './faa.json')
shutil.move('./faa.json', './buz.json')


#### File Wildcars ####

import glob

print(glob.glob('*.py'))


#### Command Line Arguments ####

import sys

print(sys.argv)

import argparse

parser = argparse.ArgumentParser(prog = 'top'
        , description = 'Show top lines from each file')
parser.add_argument('filenames', nargs = '+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()  # triggers the parsing
print(args)
args.filenames # Namespace behave like a container

#### Error Output Redirection and Program Termination ####

sys.stderr.write('Warning, log file not found starting a new one\n')
# sys.exit(-1)


#### String Patter Matching ####

import re

# https://docs.python.org/2/library/re.html
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# finds the first expression repeated
# and replace both by only the second one.
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea for too'.replace('too', 'two')


#### Mathematics ####

import math

math.cos(math.pi / 4)
math.log(1024, 2)

import random

random.choice([i for i in range(6)])
random.sample(range(100), 10)
random.random()  # [0,1)
random.randrange(10)  # [0,10)

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
mean = statistics.mean(data)
median = statistics.median(data)
variance = statistics.variance(data)
print(f'Data {data}\nMean: {mean:.3f}\nMedian: {median:.3f}\nVariance: {variance:.3f}')


##### Internet ####

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()


#### Dates and Times ####

from datetime import date
now = date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1964, 7, 31)
age = now - birthday
age.days


#### Data Compression ####


import zlib
s = b'witch which has which witches wrist watch'
len(s)  # 41

t = zlib.compress(s)
len(t)  # 37
zlib.decompress(t) == s

zlib.crc32(s)  # Checksum

#### Performance Measurement ####

from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()



import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()

# Do something
zlib.decompress(t) == s

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())


#### Quality Control ####

# Doctest

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

# Unit Testing

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests


#### More #####

import xmlrpc.client
import xmlrpc.server
import email
import poplib
import json
import sqlite3
import locale
import codecs
# ....
