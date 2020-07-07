# File: list.py 
'''creates a list from a sequence of values.A list object is a collection which is ordered and changeable.
Syntax: list(iterable)
iterable	Required. A sequence, collection or an iterator object'''

x = list(('apple', 'banana', 'cherry'))			#list from tuple
print(type(x))
#Output: <class 'list'>
print(x)
#Output: ['apple', 'banana', 'cherry']

print(list({1,3,2,2}))		#list from set
#Output:[1, 2, 3]
