# File: ascii.py
'''Returns a readable version of an object or a printable representation of a python object (like String, List, Tuple, Dictionary etc). 
Replaces none-ascii characters with escape character (backslash (\))'''




print(ascii('a'))
#Output:- 'a'

print(ascii(10000))
#Output:- 10000

print(ascii(3*6))
#Output:- 18

print(ascii(''))
#Output:- ''

print(ascii('   '))
#Output:- '   '

print(ascii('$'))
#Output:- '$'

'''print(ascii(list['1',1,('a','b','c')]))
#Output:- 'type' object is not subscriptable'''

print(ascii(['1',1,('a','b','c')]))
#Output:- ['1',1,('a','b','c')]

#--------NON ASCII Charecter-----------

print(ascii('å'))
#Output:- '\xe5'

print(ascii('1. å is an ascii char'))
#Output:- '1. \xe5 is an ascii char'

print(ascii('ș'))
#Output:- '\u0219'

print(ascii('ușer'))
#Output:- 'u\u0219er'




