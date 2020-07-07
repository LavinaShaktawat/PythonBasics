# File: bin.py
# Returns the binary version of a integer number 

print(bin(0))
#Output:-	0b0

print(bin(1))
#Output:-	0b1

print(bin(-1))
#Output:-	-0b1

print(bin(+256))
#Output:-	0b100000000

print(bin(256000000000))
#Output:-	0b11101110011010110010100000000000000000

print(bin('256'))
#Output:-	TypeError: 'str' object cannot be interpreted as an integer

print(bin('a'))
#Output:-	TypeError: 'str' object cannot be interpreted as an integer

print(bin(.111))
#Output:-	TypeError: 'float' object cannot be interpreted as an integer