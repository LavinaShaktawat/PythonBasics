# File: zip.py 
'''Returns an iterator, from two or more iterators.
	The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
	
	If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
Syntax: 	zip(iterator1, iterator2, iterator3 ...)
	iterator1, iterator2, iterator3 ...			Iterator objects that will be joined together'''

print(set(zip([1,2],[3,4,5])))
#Output:{(2, 4), (1, 3)}

print(set(zip([1,2,3],['a','b','c'])))
#Output:{(2, 'b'), (1, 'a'), (3, 'c')}


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

print(set(zip(a, b)))
#Output:{('Mike', 'Monica'), ('John', 'Jenny'), ('Charles', 'Christy')}

#To unzip this, we write the following code.

x,y,z=a
print(x)
#Output: John
print(y)
#Output: Charles
print(z)
#Output: Mike

x,y,z=b
print(x)
#Output: Jenny
print(y)
#Output: Christy
print(z)
#Output: Monica
