# File: open.py
'''Opens a file and returns a file object.open() lets us open a file. 
Syntax: open(file, mode)
	file	The path and name of the file
	mode	A string, define which mode you want to open the file in:
	"r" - Read - Default value. Opens a file for reading, error if the file does not exist
	"a" - Append - Opens a file for appending, creates the file if it does not exist
	"w" - Write - Opens a file for writing, creates the file if it does not exist
	"x" - Create - Creates the specified file, returns an error if the file exist
	
	In addition you can specify if the file should be handled as binary or text mode
	"t" - Text - Default value. Text mode
	"b" - Binary - Binary mode (e.g. images'''

# Open file in write mode and add content in file
f = open("testFile.txt", "w")
print(f.write('This lines are write by python program ,using write mode.'))
#Output: 57 	#Opens the named file which is exists in same folder and write into this file all old content will delete  automatically and return no of characters which are written.

# Open file in read mode and read content from file
f = open("E:\\testFile.txt","rt")		#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
print(f.read())
'''#Output:- 
This lines are write by python program ,using write mode'''

# Open file in read mode and read content from file
f = open("testFile.txt", "r")
print(f.read())
'''#Output:- 
This lines are write by python program ,using write mode'''

# Open file in append mode and add content in file
f = open("testFile.txt", "a")
print(f.write("\nThis is newly added line, using append mode."))
#Output: 45	 #Opens the named file which is exists in same folder and append content having length 45 characters into it.

# Open file in read mode and read content from file
f = open("testFile.txt", "r")
print(f.read())
'''#Output:- 
This lines are write by python program ,using write mode.
This is newly added line, using append mode.'''

# Open file in create mode and add content in file
f = open("testFile.txt", "x")
print(f.write('This file created using create mode'))
#Output: FileExistsError: [Errno 17] File exists: 'testFile.txt'	//through error when same file already exists otherwise create new file with specified name

# Open file in create mode content in file
f = open("testFilecreate.txt", "x")
print(f.write('This file created using create mode'))
#output: 35		 #Creates new file and added specified content having length 35 to it 

f= open('testFilecreate.txt')
print(type(f))
#Output: <class '_io.TextIOWrapper'>
print(f.read())
#Output: This file created using create mode


'''import os
os.chdir('C:\\Users\\lifei\\Desktop')	'''
