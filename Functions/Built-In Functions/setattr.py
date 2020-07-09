# File: setattr.py
''' sets the value of the specified attribute of the specified object.
Syntax:		setattr(object, attribute, value)
	object			Required. An object.
	attribute		Required. The name of the attribute you want to set
	value			Required. The value you want to give the specified attribute'''
	
class Person:
  name = "Lavina"
  age = 26
  country = "India"

obj = Person()  
print(obj.age)
#Output:26
  
setattr(Person, 'age', 28)
print(obj.age)
#Output:28