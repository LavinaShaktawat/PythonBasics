# File: type.py 
'''Returns the type of an object i.e. the type() function to check the type of object we’re dealing with.
Syntax:	type(object, bases, dict)
	object		Required. If only one parameter is specified, the type() function returns the type of this object
	bases		Optional. Specifies the base classes
	dict		Optional. Specifies the namespace with the definition for the class'''

print(type('abcdefgh'))
#Output: <class 'str'>	

print(type(1,))
#Output: 	<class 'int'>
		
	
print(type({}))
#Output: <class 'dict'>

print(type(set()))
#Output:	<class 'set'>

print(type((1,2,3)))
#Output: 	<class 'tuple'>

print(type([1,'','a']))
#Output: 	<class 'list'>

print(type(()))
#Output: 	<class 'tuple'>

print(type(False))
#Output: <class 'bool'>	
