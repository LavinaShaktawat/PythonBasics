# File: object.py
'''Returns a new featureless/empty object.
	You cannot add new properties or methods to this object.
	This object is the base for all classes, it holds the built-in properties and methods which are default for all classes.
Syntax: object()'''

o=object()
print(type(o	# type() tells us that it’s an object.
#Output:<class 'object'>

print(dir(o))	# dir() tells us the object’s attributes. But since this does not have the __dict__ attribute, we can’t assign to arbitrary attributes.

#Output:['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']