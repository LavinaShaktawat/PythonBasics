# File: max.py
'''The max() function returns the item with the highest value, or the item with the highest value in an iterable.
	If the values are strings, an alphabetically comparison is done.
Syntax: max(n1, n2, n3, ...)			Or:			max(iterable)
	n1, n2, n3, ...		One or more items to compare
	iterable			An iterable, with one or more items to compare'''
	
print(max(25,98,98.9))
#Output:98.9

#values are strings, an alphabetically comparison is done.
print(max('99','108','5567','34645657'))
#Output:99

print(max('Lavina','Eshal','Rituraj','Solanki'))
#Output:Solanki

print(max('hello','Hello'))
#Output:hello

print(max([1,2,3,4,5]))
#Output:5

myset={103,3456,567,879,234}
print(max(myset))
#Output:3456







