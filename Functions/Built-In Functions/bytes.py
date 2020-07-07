# File: bytes.py
# Returns a immutable bytes object.
'''It can convert objects into bytes objects, or create empty bytes object of the specified size.
The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
Syntax:- bytes(x, encoding, error)
X=	A source to use when creating the bytes object.
	If it is an integer, an empty bytes object of the specified size will be created.
	If it is a String, make sure you specify the encoding of the source.
encoding=	The encoding of the string
error=	Specifies what to do if the encoding fails.'''

print(bytes(4))
#Output:- b'\x00\x00\x00\x00'

print(bytes('abc','utf-8'))
#Output:- b'abc'

print(bytes(1))
#Output:- b'\x00'

print(bytes(0))
#Output:- b''

byts=bytes(4)	#bytes(b'\x00\x00\x00\x00')
byts.append(1)
print(byts)
#Output:- AttributeError: 'bytes' object has no attribute 'append'

byts=bytes(4)	
byts[0]=1
byts[2]=7
print(byts)
#Output:- TypeError: 'bytes' object does not support item assignment

print(bytes(4.0))
#Output:- TypeError: cannot convert 'float' object to bytes

print(bytes(-4))
#Output:- ValueError: negative count

a="this is my code"
print(bytes(a))
#Output:- TypeError: string argument without an encoding


#--------- bytearray with list----------
byts=bytes([1,2,3,4,5])
print(byts)
#Output:- b'\x01\x02\x03\x04\x05'

byts=bytes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
print(byts)
#Output:- b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15'

byts=bytes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,'a','abc'])
print(byts)
#Output:- TypeError: 'str' object cannot be interpreted as an integer