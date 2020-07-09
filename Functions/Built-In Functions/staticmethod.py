# File: staticmethod.py 
''' Staticmethod or syntactic sugar @staticmethod  converts a method into a static method.
A static method is bound to a class rather than to an object. But it can be called on the class or on an object.'''

class Fruit:
	def fruit_name(x):
		print('this is {0}'.format(x))

obj = staticmethod(Fruit.fruit_name)
#print(obj)
#Output:	<staticmethod object at 0x01328148>
Fruit.fruit_name('Apple')
#Output:	 this is Apple


#using the syntactic sugar @staticmethod like this:-

class Fruit:
	@staticmethod
	def fruit_name(x):
		print('this is {0}'.format(x))
		
Fruit.fruit_name('Orange')
#Output:	this is Orange