# File: len.py 
'''returns the length of an object or  number of items in an object.
When the object is a string, the len() function returns the number of characters in the string..
Syntax: len(object)
object		Required. An object. Must be a sequence or a collection'''

mystr = "Hello"
print(len(mystr))
#Output: 5

mylst=['Apple','orange','grapes','pineapple']
print(len(mylst))
#Output: 5

print(len({'1,',2,'4'}))
#Output: 3

print(len({'1,',2,'4','4'}))
#Output: 3 		Here, we get 3 instead of 4, because the set takes the value 4 only once.

print(len(['1',2,'4','4']))
#Output: 4 		