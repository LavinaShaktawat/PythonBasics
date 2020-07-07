# File: hash.py 

#Returns the hash value of a specified object.Returns the hash value of a specified object

class Person:
	age='26'
	name='Lavina'
	country='India'

print(hash(Person))
#Output: 686880

x='abc'
print(hash(x))
#Output: 761753617

print(hash('abc'))
#Output: 761753617

print(hash(123))
#Output: 123

print(hash(True))
#Output: 1

print(hash(False))
#Output: 0

