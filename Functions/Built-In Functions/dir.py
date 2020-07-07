# File: dir.py

'''Returns a list of the specified object's properties and methods or returns an object’s attributes.
Syntax: dir(object)
object	The object you want to see the valid attributes of

class Fruit:
	size=7
	color='red'
	
apple= Fruit()
print(apple)
#Output:- <__main__.Fruit object at 0x00F88178>

print(dir(apple))
#output:-['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'size']
