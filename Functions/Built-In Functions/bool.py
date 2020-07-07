# File: bool.py
'''Returns the boolean value of the specified object
The object will always return True, unless: The object is empty(like [], (), {}),  False,0, None'''

print(bool(1))
#Output:- True

print(bool(0))
#Output:- False

print(bool(''))
#Output:- False

print(bool(0.5))
#Output:- True

print(bool(-0.5))
#Output:- True

print(bool(False))
#Output:- False

print(bool())
#Output:- False

print(bool(()))
#Output:- False

print(bool({}))
#Output:- False

print(bool(None))
#Output:- False