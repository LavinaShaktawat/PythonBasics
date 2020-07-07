# File: exec.py

'''Executes or runs the specified Python code (or object) dynamically.
The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression.
Syntax: exec(object, globals, locals)
object	A String, or a code object
globals	Optional. A dictionary containing global parameters
locals	Optional. A dictionary containing local parameters'''

x = 'name = "John"\nprint(name)'
exec(x)
#Output: John

exec('a=2;b=3;print(a+b)')
#Output: 5

exec(input('Enter your name'))
#Output: Enter your nameprint('Lavina')
#Lavina