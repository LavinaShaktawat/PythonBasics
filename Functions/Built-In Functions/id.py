# File: id.py 
'''Returns the unique identity of specified object.All objects in Python has its own unique id.
The id is assigned to the object when it is created.
The id is the object's memory address, and will be different for each time you run the program. (except for some object that has a constant unique id, like integers from -5 to 256)
Syntax: id(object)
object		Any object, String, Number, List, Class etc.'''

x=['Apple','banana','Orange']
print(id(x))
#Output:8780712

print(id(x))
#Output:12057512

print(id(1))
#Output:1831598000

print(id('abd'))
#Output:44739648


if id({1,2,3})==id({1,3,2}) :
	print(True)
else:
	print(False)
	
#Output: True