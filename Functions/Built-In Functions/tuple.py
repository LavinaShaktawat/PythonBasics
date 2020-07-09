# File: tuple.py 
'''The tuple() function creates a tuple object.
Note: You cannot change or remove items in a tuple.
Syntax:	tuple(iterable)
	iterable	Required. A sequence, collection or an iterator object
'''

tpl= tuple((1,2,3,4))
print(tpl)
#Output:	(1, 2, 3, 4)
	
#creating tuple from list
print(tuple(['apple', 'banana', 'cherry']))
#Output:	('apple', 'banana', 'cherry')