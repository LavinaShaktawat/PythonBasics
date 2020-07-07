# File: bytearray.py
#Returns an array of bytes i.e. returns a python array of a given byte size.
'''Syntax:- bytearray(x, encoding, error)
X=	A source to use when creating the bytearray object.
	If it is an integer, an empty bytearray object of the specified size will be created.
	If it is a String, make sure you specify the encoding of the source.
encoding=	The encoding of the string
error=	Specifies what to do if the encoding fails.
'''

print(bytearray(4))
#Output:- bytearray(b'\x00\x00\x00\x00')

print(bytearray('abc','utf-8'))
#Output:- bytearray(b'abc')

print(bytearray(1))
#Output:- bytearray(b'\x00')

print(bytearray(0))
#Output:- bytearray(b'')

bytary=bytearray(4)		#bytearray(b'\x00\x00\x00\x00')
print(bytary.append(1))
#Output:- None

bytary=bytearray(4)	
bytary.append(1)
print(bytary)
#Output:- bytearray(b'\x00\x00\x00\x00\x01')

bytary=bytearray(4)	
bytary.append(1)
bytary[0]=1
print(bytary)
#Output:- bytearray(b'\x01\x00\x00\x00\x01')

bytary=bytearray(4)	
bytary.append(1)
bytary[0]=1
bytary[2]=7
print(bytary)
#Output:- bytearray(b'\x01\x00\x07\x00\x01')

print(bytearray(4.0))
#Output:- TypeError: cannot convert 'float' object to bytearray

print(bytearray(-4))
#Output:- ValueError: negative count

a="this is my code"
print(bytearray(a))
#Output:- TypeError: string argument without an encoding

print(bytearray('a'))
#Output:- TypeError: string argument without an encoding

#--------- bytearray with list----------
bytary=bytearray([1,2,3,4])
print(bytary)
#Output:- bytearray(b'\x01\x02\x03\x04')

bytary=bytearray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
print(bytary)
#Output:- bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15')

bytary=bytearray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,'a','abc'])
print(bytary)
#Output:- TypeError: 'str' object cannot be interpreted as an integer


