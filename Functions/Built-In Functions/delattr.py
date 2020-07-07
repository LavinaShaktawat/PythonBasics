# File: delattr.py
''' Deletes the specified attribute (property or method) from the specified object
 Syntax: delattr(object, attribute)
object		Required. An object.
attribute	Required. The name of the attribute you want to remove'''


class fruit:	
	size=7

apple = fruit()
print(apple.size)
#Output: 7
delattr(apple,size)
print(apple.size)
#Output: NameError: name 'size' is not defined