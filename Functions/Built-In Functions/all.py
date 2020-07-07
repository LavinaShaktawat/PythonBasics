# File: all.py
'''The all() function takes a container as an argument. 
This Built in Functions returns True if all values in a python iterable have a Boolean value of True. 
An empty value has a Boolean value of False.
An iterable object are- list, tuple, dictionary,set'''

#------------ Check if all items in a list are True:----------------
lst=[True,True,True]
res=all(lst)
print(res)
#output: False

lst=[True,True,False]
res=all(lst)
print(res)
#output: False

lst=[0,1,'3']
res=all(lst)
print(res)
#output: False

lst=[0,1,2]
res=all(lst)
print(res)
#output: False

lst=[1,2,3]
res=all(lst)
print(res)
#output: True

lst=['a','b','c']
res=all(lst)
print(res)
#output: True

lst=['a','b',0]
res=all(lst)
print(res)
#output: False

lst=['a','b',-1]
res=all(lst)
print(res)
#output: True

#------------ Check if all items in a tuple are True:----------------
tpl = (0, True, False)
res = all(tpl)
print(res)
#output: False

tpl=('*','','')
res=all(tpl)
print(res)
#output: False

tpl=(' ',' ',' ')
res=all(tpl)
print(res)
#output: True

#------------ Check if all items in a Set are True:----------------
myset = {0, True, True}
res = all(myset)
print(res)
#output: False

#------------ Check if all items in a Dictionary are True:----------------
#When used on a dictionary, the all() function checks if all the keys are true, not the values.
dct = {0:'Apple', 1:'Boy', 2:3,3:[1,2,3]}
res = all(dct)
print(res)
#output: False

dct = {1:'Apple', 2:'Boy', 3:3,4:[1,2,3]}
res = all(dct)
print(res)
#output: True
