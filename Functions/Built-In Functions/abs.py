# File: abs.py
'''The abs() is one of the most popular Python built-in functions, which returns the absolute value of a number. 
A negative value’s absolute is that value is positive.'''
num= 9
print(abs(num)) 
#output: 7

num= -7
print(abs(num)) 
#output: 7

num=0
print(abs(num))
#output: 0

num=0.123
print(abs(num))
#output: 0.123

num='hello'
print(abs(num))
#output: TypeError: bad operand type for abs(): 'str'