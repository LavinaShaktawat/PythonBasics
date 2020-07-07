# File: memoryview.py
''' Returns a memory view object from a specified object.i.e shows us the memory view of an argument.
Syntax: memoryview(obj)
	obj			A Bytes object or a Bytearray object.'''
#Create and print a memoryview object:	
x = memoryview(b"Hello")
print(x)
#Output:	<memory at 0x0051FB08>
#return the Unicode of the first character
print(x[0])
#Output: 72
#return the Unicode of the second character
print(x[1])
#Output: 101

print(x[2])
#Output: 108

print(x[3])
#Output: 108

print(x[4])
#Output: 111

'''print(x[5])
#Output: IndexError: index out of bounds on dimension 1'''

a=bytes(4)
print(memoryview(a))
#Output: <memory at 0x00E3FE68>
 
for i in memoryview(a):
	print(i)
'''#Output: 0
0
0
0'''
