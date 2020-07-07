# File: hasattr.py 

'''Returns True if the specified object has the specified attribute (property/method)
Syntax: hasattr(object, attribute)
object	Required. An object.
attribute	The name of the attribute you want to check if exists'''

class Person:
	age='26'
	name='Lavina'
	country='India'
	
x= hasattr(Person,'age')
print(x)
#Output: True

x= hasattr(Person,'weight')
print(x)
#Output: False

