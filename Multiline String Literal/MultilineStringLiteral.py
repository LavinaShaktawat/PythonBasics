# File: MultilineStringLiteral.py

# Multiline String Literals can be created using triple delimeter

# Exe 1:- using single quote
str ='''\t Multiline strings are not comments although can be used as such with special comment called Docstrings. \n  Doc strings are used for documentation purpose.'''
print(str)
#Output:-
#         Multiline strings are not comment although can be used as such with special comment called Docstrings.
#  Doc strings are used for documentation purpose.

# Exe 2:- using double quote
str2="""When Python compiles the code then these docstrings are also the part of code.\n Whereas comments are ignored.
		New line and tab are part of string.
 """
print(str2)
#Output:- 
#When Python compiles the code then these docstrings are also the part of code.
# Whereas comments are ignored.
#               New line and tab are part of string.

	
