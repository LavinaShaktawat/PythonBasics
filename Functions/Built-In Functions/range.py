# File: range.py
'''Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
Syntax: range(start, stop, step)
	start	Optional. An integer number specifying at which position to start. Default is 0
	stop	Required. An integer number specifying at which position to stop (not included).
	step	Optional. An integer number specifying the incrementation. Default is 1'''
	
#Create a sequence of numbers from 3 to 5, and print each item in the sequence:
for n in range(3, 6):
  print(n)
'''Output: 
3
4
5'''

#Create a sequence of numbers from 1 to 10, but increment by 3 instead of 1:
for n in range(1,10,3):
	print(n)
'''Output: 
1
4
7'''

#Create a sequence of numbers from 100 to 50, but decrement by 10:
for n in range(100,50,-10):
	print(n)
'''Output: 
100
90
80
70
60'''