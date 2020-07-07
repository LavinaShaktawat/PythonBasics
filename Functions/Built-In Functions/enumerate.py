# File: enumerate.py
'''Takes a collection (e.g. a tuple) and returns it as an enumerate object
The enumerate() function adds a counter as the key of the enumerate object.
Syntax: 
enumerate(iterable, start)
iterable	An iterable object
start		A Number. Defining the start number of the enumerate object. Default 0'''

x= ('apple', 'banana', 'cherry')
print(enumerate(x))
#Output: <enumerate object at 0x009E6628>

for i in enumerate(x):
	print(i)
#Output: 
'''(0, 'apple')
(1, 'banana')
(2, 'cherry')'''
