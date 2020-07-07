# File: iter.py 
'''Returns a iterator for an object.
Syntax: iter(object, sentinel)
	object		Required. An iterable object
	sentinel	Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel '''
	
for i in iter([1,2,3]):
	print(i)
'''Output:
1
2
3'''

x= iter(["Apple",'Orange','Banana'])
print(next(x))
#Output: Apple
print(next(x))
#Output: Orange
print(next(x))
#Output: Banana