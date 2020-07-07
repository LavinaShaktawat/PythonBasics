# File: dict.py
'''The dict() function creates a dictionary.A dictionary is a collection which is unordered, changeable and indexed.
Syntax: dict(keyword arguments)
keyword arguments	Required. As many keyword arguments you like, separated by comma: key = value, key = value ...'''


print(dict())
#Output:{}

print(dict([(1,3),(4,5),(6,7)]))
#OutPut: {1: 3, 4: 5, 6: 7}

print(dict(name='Lavi',age=26,country='India'))
#OutPut: {'name': 'Lavi', 'age': 26, 'country': 'India'}