# File: classmethod.py
#Converts a method into a class method. Then, we call it like we would call any static method in python without an object.


class fruit:
	def fruit_name(self):
		print('I am ', format(self))
		
fruit.fruit_name = classmethod(fruit.fruit_name('Apple'))

fruit.fruit_name()

#Output: 	I am Apple
#			TypeError: 'NoneType' object is not callable