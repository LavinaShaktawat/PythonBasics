# File: map.py
'''Returns the specified iterator with the specified function applied to each item.
The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
Like filter() it maps True or False values on each item in the iterable.
Syntax: map(function, iterables)
	function	Required. The function to execute for each item
	iterable	Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.'''
def get_length(n):
  return len(n)
x= map(get_length, ('apple', 'banana', 'cherry'))
print(x)
#Output: <map object at 0x00BC81D8>

x= list(map(get_length, ('apple', 'banana', 'cherry')))
print(x)
#Output: [5, 6, 6]

#Make new fruits by sending two iterable objects into the function:
def addstr(a, b):
  return a + b

x = list(map(addstr, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))
print(x)
#Output:['appleorange', 'bananalemon', 'cherrypineapple']

print(list(map(lambda x:x%2==0,[1,2,3,4,5])))
#Output:[False, True, False, True, False]

