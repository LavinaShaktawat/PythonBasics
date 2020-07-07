# File: pow.py
'''pow() takes two arguments- say, x and y. It then returns the value of x to the power of y.
If a third parameter is present, it returns x to the power of y, modulus z.
Syntax:	pow(x, y, z)
	x	A number, the base
	y	A number, the exponent
	z	Optional. A number, the modulus
'''
print(pow(3,4))
#Output: 81

print(pow(7,0))
#Output: 1

print(pow(7,-1))
#Output: 0.14285714285714285

#Return the value of 2 to the power of 3, modulus 5 (same as (2 * 2 * 2) % 5):
x = pow(2, 3, 5)
print(x)
#Output:	3