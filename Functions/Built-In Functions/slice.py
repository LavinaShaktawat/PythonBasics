# File: slice.py
'''returns a slice object that represents the set of indices specified by range(start, stop, step).
A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.
Syntax:	slice(start, end, step)
	start		Optional. An integer number specifying at which position to start the slicing. Default is 0
	end			An integer number specifying at which position to end the slicing
	step		Optional. An integer number specifying the step of the slicing. Default is 1'''
	
print(slice(2,7,2))
#Output: slice(2, 7, 2)

print('PYTHON'[slice(1,6,2)])
#Output: YHN

#Create a tuple and a slice object. Use the slice object to get only the two first items of the tuple:
a = ("l", "a", "v", "i", "n", "a")
x = slice(2)
print(a[x])
#Output: ('l', 'a')

#Create a tuple and a slice object. Start the slice object at position7, and slice to position 16, and return the result:
tpl=('L','A','V','I','N','A','-','S','H','A','K','T','A','W','A','T')
print(tpl[slice(7,16)])
#Output: ('S', 'H', 'A', 'K', 'T', 'A', 'W', 'A', 'T')

#Create a tuple and a slice object. Use the step parameter to return every second item:
tpl=('L','A','V','I','N','A','-','S','H','A','K','T','A','W','A','T')
print(tpl[slice(0,16,2)])
#Output: ('L', 'V', 'N', '-', 'H', 'K', 'A', 'A')