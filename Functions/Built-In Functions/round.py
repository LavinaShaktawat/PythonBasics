# File: round.py
'''The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
	The default number of decimals is 0, meaning that the function will return the nearest integer.
Syntax:	round(number, digits)
	number	Required. The number to be rounded
	digits	Optional. The number of decimals to use when rounding the number. Default is 0'''
#Round to the nearest integer:
print(round(568.71456))
#Output: 569

#Round a number to only two decimals:
print(round(568.71723556,4))
#Output: 568.7172

print(round(568.71456,-1))
#Output: 570.0

print(round(568,-1))
#Output: 570

print(round(3.7,-1))
#Output: 0.0

print(round(5.7,-1))
#Output: 10.0
#round of by -1 will round the number to nearest 10's integer

print(round(55.5,-1))
#Output: 100.0