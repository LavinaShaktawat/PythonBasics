# File: isinstance.py 
''' The isinstance() function returns True if the specified object is of the specified type, otherwise False.
	If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
Syntax: isinstance(object, type)
	object		Required. An object.
	type		A type or a class, or a tuple of types and/or classes'''
	
# check a number is instanse of type int
print(isinstance(5, int))
#Output: True

print(isinstance(5.4, int))
#Output: False
	
#Check if "Hello" is one of the types described in the type parameter:
print(isinstance("Hello", (float, int, str, list, dict, tuple)))
#Output: True

#Check if org is an instance of Orange class:
class Orange:
	size=7
	color='orange'

org = Orange()
print(isinstance(org,Orange))
#Output: True

