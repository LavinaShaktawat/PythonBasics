# File: vars.py 
'''the vars() function returns the __dic__ attribute of an object.
The __dict__ attribute is a dictionary containing the object's changeable attributes.
Note: calling the vars() function without parameters will return a dictionary containing the local symbol table.
Syntax:	vars(object)
object	Any object with a __dict__attribute'''

class Person:
  name = "Lavina"
  age = 26
  country = "India"

print(vars(Person))
#Output:{'__module__': '__main__', 'name': 'Lavina', 'age': 26, 'country': 'India', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

print(vars())
#Output:{'__module__': '__main__', 'name': 'Lavina', 'age': 26, 'country': 'India', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}{'__name__': '__main__', '__doc__': "the vars() function returns the __dic__ attribute of an object.\nThe __dict__ attribute is a dictionary containing the object's changeable attributes.\nNote: calling the vars() function without parameters will return a dictionary containing the local symbol table.\nSyntax:\tvars(object)\nobject\tAny object with a __dict__attribute", '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0084AF70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\PythonPrgrams\\PythonBasics\\Functions\\Built-In Functions\\vars.py', '__cached__': None, 'Person': <class '__main__.Person'>}
