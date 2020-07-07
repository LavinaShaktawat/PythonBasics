# File: ord.py
'''returns the number representing the unicode code of a specified character. 
Syntax: ord(character)
	character	 any character or string having length 1
note:- Convert back to character with the chr() function.'''

print(ord('l'))
#Output:108

print(ord('2'))
#Output: 50

print(ord('12'))
#Output: ord() expected a character, but string of length 2 found

print(ord('lavina'))
#Output: ord() expected a character, but string of length 6 found

print(ord(12))
#Output: ord() expected string of length 1, but int found

