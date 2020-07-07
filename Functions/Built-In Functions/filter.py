# File: filter.py
'''Use a filter function to exclude items in an iterable object i.e.  filters out the items for which the condition is True.
Syntax: filter(function, iterable)
function	A Function to be run for each item in the iterable
iterable	The iterable to be filtered'''

print(list(filter(lambda x:x%2==0,[1,2,0,False])))
#Output:[2, 0, False]

print(list(filter(lambda x:x%2!=0,[1,2,0,False])))
#Output:[1]

#Filter the array, and return a new array with only the values equal to or above 18:
age=[5,12,10,17,18,21,9,23]

def my_func(x):
	if x<18:
		return False
	else: 
		return True

adults = filter(my_func,age)
print (adults)
#Output: <filter object at 0x015081D8>
for x in adults:
	print(x)
#Output: 18,21,23
