# File: int.py 
''' int() function converts the specified value into an integer number.
Syntax: int(value, base)
value	A number or a string that can be converted into an integer number
base	A number representing the number format. Default value: 10'''

print(int(1.645))
#Output: 1

print(int(-1.645))
#Output: -1

print(int("1645"))
#Output: 1645

print(int("1645",10))
#Output: 1645

print(int("1645",8))
#Output: 933

print(int("0",2))
#Output: 0

print(int("1",2))
#Output: 1

print(int("1645",16))
#Output: 5701

print(int("2",2))
#Output: ValueError: invalid literal for int() with base 2: '2'

#print(int("1.645",16))
#Output: ValueError: invalid literal for int() with base 16: '1.645'

