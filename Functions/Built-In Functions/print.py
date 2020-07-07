# File: print.py
'''The print() function prints the specified message to the screen, or other standard output device.
	The message can be a string, or any other object, the object will be converted into a string before written to the screen.
Syntax: 	print(object(s), sep=separator, end=end, file=file, flush=flush)
	object(s)			Any object, and as many as you like. Will be converted to string before printed
	sep='separator'		Optional. Specify how to separate the objects, if there is more than one. Default is ' '
	end='end'			Optional. Specify what to print at the end. Default is '\n' (line feed)
	file				Optional. An object with a write method. Default is sys.stdout
	flush				Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False'''
	
#Print more than one object:

print("Hello", "how are you?")
#Output: Hello how are you?

#Print two messages, and specify the separator:
print("Hello", "how are you?", sep="---")
#Output: Hello---how are you?

#Print two messages, and specify end:
print("Hello", "how are you?", sep="---",end="^^^")
#Output: Hello---how are you?^^^

#Print two messages, and specify end:
print("Hello", "how are you?", sep="---",end="^^^")
#Output: Hello---how are you?^^^