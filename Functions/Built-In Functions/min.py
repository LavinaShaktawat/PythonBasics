# File: min.py
'''The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
	If the values are strings, an alphabetically comparison is done.
Syntax: min(n1, n2, n3, ...)			Or:			min(iterable)
	n1, n2, n3, ...		One or more items to compare
	iterable			An iterable, with one or more items to compare'''
	
print(min(25,98,98.9))
#Output:25

#values are strings, an alphabetically comparison is done.
print(min('99','108','5567','34645657'))
#Output:108

print(min('Lavina','Eshal','Rituraj','Solanki'))
#Output:Eshal

print(min('hello','Hello'))
#Output:Hello

print(min([1,2,3,4,5]))
#Output:1

myset={103,3456,567,879,234}
print(min(myset))
#Output:103

print(min([1,2,3,4,5]))
#Output:1







