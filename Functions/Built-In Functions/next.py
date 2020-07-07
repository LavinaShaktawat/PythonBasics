# File: next.py
'''returns the next element from the iterator.
	when we traversed all items, and we call next(), it raises StopIteration.You can add a default return value, to return if the iterable has reached to its end.
Syntax: next(iterable, default)
	iterable	Required. An iterable object.
	default		Optional. An default value to return if the iterable has reached to its end.'''

#Create an iterator, and print the items one by one:

mylist = iter(["apple", "banana", "cherry"])
print(next(mylist))
#Output:apple
print(next(mylist))
#Output:banana
print(next(mylist))
#Output:cherry
print(next(mylist))
#Output:StopIteration


#Return a default value when the iterable has reached to its end:
mylist = iter(["apple", "banana", "cherry"])
print(next(mylist, "orange"))
#Output:apple
print(next(mylist, "orange"))
#Output: banana
print(next(mylist, "orange"))
#Output: cherry
print(next(mylist, "orange"))
#Output: orange

