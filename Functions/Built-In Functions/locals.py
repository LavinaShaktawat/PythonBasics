# File: locals.py 
'''Returns an updated dictionary of the current local symbol table in other words this returns the local symbol table as a dictionary.
	A symbol table contains necessary information about the current program.
Syntax:  locals()'''
#Get the filename of the current program:
x = locals()
print(x)
#Output: {'__name__': '__main__', '__doc__': 'Returns an updated dictionary of the current local symbol table in other words this returns the local symbol table as a dictionary.\n\tA symbol table contains necessary information about the current program.\nSyntax:  locals()', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0139AF70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\PythonPrgrams\\PythonBasics\\Functions\\Built-In Functions\\locals.py', '__cached__': None, 'x': {...}}
