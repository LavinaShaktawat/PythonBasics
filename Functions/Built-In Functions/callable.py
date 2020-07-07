# File: callable.py
# Returns True if the specified object is callable, otherwise False

print(callable(str))
#Output: True

print(callable(list))
#Output: True

print(callable(set))
#Output: True

print(callable(int))
#Output: True

print(callable(tuple))
#Output: True

print(callable(float))
#Output: True

print(callable('abc'))
#Output: False

num=10
print(callable(num))
#Output: False

print(callable(callable))
#Output:true

#-------- Callable with UD Function ----------
def test_func():
	print('test Function')
	
print(callable(test_func))
#Output: true

#-------- Callable with Builtin function ----------
print(callable(len))
#Output: true

#-------- Callable with class ----------
class MyClass:
	def __init__(self):
		print('I am in MyClass')
	
print(callable(MyClass))	
#Output: true

cls = MyClass	#assigning MyClass to cls
print(callable(cls))
#Output: true

inst_cls = MyClass()	#create Instance of MyClass
print(callable(inst_cls))
#Output: I am in MyClass
#False
inst_cls()
#Output: TypeError: 'MyClass' object is not callable

