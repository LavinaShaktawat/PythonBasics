# File: eval.py

''' This Function takes a string as an argument, which is Evaluates and executes an expression as an expression.
Syntax: eval(expression, globals, locals)
expression	A String, that will be evaluated as Python code
globals	Optional. A dictionary containing global parameters
locals	Optional. A dictionary containing local parameters'''


x=7
print(eval('x+7'))
#Output: 14

print(eval('x+(x*7)'))
#Output: 56
