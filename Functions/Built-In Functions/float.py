# File: float.py
'''Returns a floating point number
Syntax: float(value)
value	A number or a string that can be converted into a floating point number'''

print(float(0))
#Output: 0.0

print(float(.57))
#Output: 0.57

print(float(1.89))
#Output: 1.89

print(float(-4.777777777777777))
#Output: -4.777777777777777

print(float(257))
#Output: 257.0

print(float('356'))
#Output: 356.0

print(float(False))
#Output: 0.0

print(float(True))
#Output: 1.0

print(float('asdgf'))
#Output: ValueError: could not convert string to float: 'asdgf'