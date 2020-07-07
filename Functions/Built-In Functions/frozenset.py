# File: frozenset.py
'''returns an immutable frozenset object.The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
Syntax: frozenset(iterable)
iterable	An iterable object, like list, set, tuple etc.'''

print(frozenset((3,2,4)))
#Output: frozenset({2, 3, 4})

#Freeze the list, and make it unchangeable:

mylist=['apple','banana','orange']
print(mylist)
#Output:['apple', 'banana', 'orange']
x=mylist
x.append('pineapple')
print(x)
#Output:['apple', 'banana', 'orange', 'pineapple']
x=frozenset(mylist)
print(x)
#Output:frozenset({'orange', 'apple', 'pineapple', 'banana'})

x.append('grapes')
print(x)
#Output: AttributeError:'frozenset' object has no attribute 'append'

x[1]='strawberry'
print(x)
#Output: TypeError: 'frozenset' object does not support item assignment