# File: getattr.py
''' returns the value of the specified attribute from the specified object.
Syntax: getattr(object, attribute, default)
object		Required. An object.
attribute	The name of the attribute you want to get the value from
default		Optional. The value to return if the attribute does not exist'''

#Get the value of the "age" property of the "Person" object:
class Person:
	name='Lavina'
	age='26'
	place='Mumbai'

person_name= getattr(Person,'name')
print(person_name)
#Output:Lavina

#Use the "default" parameter to write a message when the attribute does not exist:

pagenumber= getattr(Person,'Page','Page attribute does not exists')
print(pagenumber)
#Output:Page attribute does not exists
