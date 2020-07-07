# File: complex.py
'''Returns a complex number
Syntax: complex(real, imaginary)

Parameter	Description
real		Required. A number representing the real part of the complex number. Default 0. 
			The real number can also be a String, like this '3+5j', when this is the case, the second parameter should be omitted.
imaginary	Optional. A number representing the imaginary part of the complex number. Default 0.'''

print(complex(1))
#Output: (1+0j)

print(complex(0))
#Output: 0j

print(complex(3.5))
#Output: (3.5+0j)

print(complex(-3.5))
#Output: (-3.5+0j)


print(complex(-3.5+0j))
#Output: (-3.5+0j)

print(complex(3,5))
#Output: (3+5j)

print(complex(-3.5+0j,7))
#Output: (-3.5+7j)

print(complex(-3.5+7j,9))
#Output: (-3.5+16j) #sum imaginary part

print(complex(3,5i))
#Output: SyntaxError: invalid syntax

print(complex(3,5,7,8))
#Output: TypeError: complex() takes at most 2 arguments (4 given)