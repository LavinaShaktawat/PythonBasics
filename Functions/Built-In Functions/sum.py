# File: sum.py 
''' takes an iterable as an argument, and returns the sum of all values.
Syntax:	sum(iterable, start)
	iterable	Required. The sequence to sum
	start		Optional. A value that is added to the return value'''
	
#Add all items in a tuple, and return the result:

a=(1,4,5,7)
print(sum(a))
#Output:	17

#Add all items in a list, and return the result:
print(sum([5,7,1,3,4]))
#Output:	20

#Start with the number 10, and add all the items in a tuple to this number:
print(sum((5,7,1,3,4), 10))
#Output:	30


print(sum(('5','7','1','3','4'), '10'))
#Output:	TypeError: sum() can't sum strings
