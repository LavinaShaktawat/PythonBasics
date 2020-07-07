# File: compile.py
'''Returns the specified Python source code as an object, ready to be executed.
We use function to convert a string code into object code.
Syntax: compile(source, filename, mode, flag, dont_inherit, optimize)
	source-			Required. The source to compile, can be a String, a Bytes object, or an AST object
	filename-		Required. The name of the file that the source comes from. If the source does not come from a file, you can write whatever you like
	mode-			Required. Legal values:
					eval - if the source is a single expression
					exec - if the source is a block of statements
					single - if the source is a single interactive statement
	flags-			Optional. How to compile the source. Default 0
	dont-inherit-	Optional. How to compile the source. Default False 
	optimize-		Optional. Defines the optimization level of the compiler. Default -1
'''

x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)
#Output: 55
		 #88
		 
x = compile('print(55)\nprint(88)', 'test', 'exec')
#Output: 

'''Here, ‘exec’ is the mode. The parameter before that is the filename for the file form which the code is read.
Finally, we execute it using exec().'''
exec(compile('a=5\nb=7\nprint(a+b)','','exec'))
#Output: 12