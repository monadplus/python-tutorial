#!/user/bin/env python3.7
# -*- coding: utf8 -*-


#####  Fancier Output Formatting ####

year = 2016
f'The current year is {year}'

yes_votes = 1/3
'Percentage of votes: {:2.2%}'.format(yes_votes)

# You can convert any variable to string using:
# * repr(): read by the interpreter
# * str(): human-readable
s = "Hello, world."
str(s)
repr(s)

#### Formatted String Literals ####

name = 'arnau'
f'At least 10 chars: {name:10}'  # adds whitespaces
# * !a  ascii()
# * !s  str()
# * !r  repr()
f'My name is {name!r}'

#### The String format() Method ####

'{1} and {0}'.format('spam', 'eggs')
'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


#### Reading and Writing Files #####

# By default is opened for text mode
#f = open('foo', 'x')  # 'a' to append instead of erasing
                       # 'r+' reading/writing
                       # 'b' for binary mode

#f.write("Should not work")
#f.close()

with open('lore.txt', 'r') as f:
    # print(f.readline())
    # print(f.read(100))
    # print(f.read())
    for line in f:
        print(line, end='')

f = open('lore.txt', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)

#### JSON ####

import json

json.dumps([1, 'simple', 'list'])

f = open('foo.json', 'r+')
json.dump(['i', 'simple', 'list'], f)
f.seek(0) # rewind
x = json.load(f)
print(x)
f.close()
