# File: issubclass.py 
'''The issubclass function takes two arguments- two python classes. If the first class is a subclass of the second, it returns True. Otherwise, it returns False.
Syntax: issubclass(class1,class2)
'''	
	
class Fruit:
	taste= 'sweet'

class Orange(Fruit):
	color='orange'
		
print(issubclass(Orange,Fruit))
#Output: True

print(issubclass(Fruit,Orange))
#Output: False

