# File: reversed.py
'''This functions reverses the contents of an iterable and returns an iterator object.
Syntax: reversed(sequence)
sequence	Required. Any iterable object'''

print(reversed('lavina'))
#Output: <reversed object at 0x01088160>

x=reversed('lavina')
for i in x:
	print(i)
'''#Output: 
a
n
i
v
a
l'''

lst=['z','y','x','w']
for itm in reversed(lst):
	print(itm)
'''#Output: 
w
x
y
z'''

print(reversed(9876543210))
#Output: TypeError: 'int' object is not reversible