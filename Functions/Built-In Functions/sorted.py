# File: sorted.py
'''returns a sorted version of an iterable. It does not, however, alter the iterable.\
The sorted() function returns a sorted list of the specified iterable object.
You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
Note: You cannot sort a list that contains BOTH string values AND numeric values.
Syntax:	sorted(iterable, key=key, reverse=reverse)
	iterable	Required. The sequence to sort, list, dictionary, tuple etc.
	key			Optional. A Function to execute to decide the order. Default is None
	reverse		Optional. A Boolean. False will sort ascending, True will sort descending. Default is False'''



a = [1, 11, 2,5,8,6.7]
x = sorted(a)
print(x)
#Output:	[1, 2, 5, 6.7, 8, 11]

a=('z','d','q','Q','E','A')
print(sorted(a))	
#Output:	['A', 'E', 'Q', 'd', 'q', 'z']	

#Sort descending:
a = ('z','d','q','Q','E','A')
x = sorted(a, reverse=True)
print(x)
#Output:	['z', 'q', 'd', 'Q', 'E', 'A']
'''print(sorted('z','d','q','Q','E','A'))
#Output:	TypeError: sorted expected 1 argument, got 6	

a = [1,'x','D', 2,5,'B','a']
x = sorted(a)
print(x)
#Output:	TypeError: '<' not supported between instances of 'str' and 'int'
'''