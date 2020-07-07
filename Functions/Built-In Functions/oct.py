# File: oct.py
'''Converts a  an integer to its octal representation.
	Octal strings in Python are prefixed with 0o.
Syntax:	oct(int)
	int		An Integer Number'''
	
print(oct(0))
#Output: 0o0

print(oct(1))
#Output: 0o1

print(oct(-256))
#Output: -0o400

print(oct(587878))
#Output: 0o2174146


print(oct('34563'))
#Output: TypeError: 'str' object cannot be interpreted as an integer

