# File: str.py 
'''The str() function takes an argument and returns the string equivalent of it.
Syntax: str(object, encoding=encoding, errors=errors)
	object		Any object. Specifies the object to convert into a string
	encoding	The encoding of the object. Default is UTF-8
	errors		Specifies what to do if the decoding fails
'''
print(str(7))
#Output: '7'

print(str(-7.8))
#Output: '-7.8'

print(str('Hello'))
#Output: 'Hello'

print(str(['a',1,'as']))
#Output: '['a', 1, 'as']'

print(str(False))
#Output: 'False'
