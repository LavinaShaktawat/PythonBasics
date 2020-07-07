# File: any.py
#Like all(), it takes one argument and returns True if, even one value in the iterable has a Boolean value of True
#Returns True if any item in an iterable object is true

#------------ Check if all items in a list are True:----------------
lst=[True,True,True]
res=any(lst)
print(res)
#output: True

lst=[False,False,False]
res=any(lst)
print(res)
#output: False

lst=[True,True,False]
res=any(lst)
print(res)
#output: True

lst=[0,1,'3']
res=any(lst)
print(res)
#output: True

lst=[0,1,2]
res=any(lst)
print(res)
#output: True

lst=[1,2,3]
res=any(lst)
print(res)
#output: True

lst=[0,0,0]
res=any(lst)
print(res)
#output: False

lst=['a','b','c']
res=any(lst)
print(res)
#output: True

lst=['a','b',0]
res=any(lst)
print(res)
#output: True

lst=['a','b',-1]
res=any(lst)
print(res)
#output: True

#------------ Check if all items in a tuple are True:----------------
tpl = (0, True, False)
res = any(tpl)
print(res)
#output: True

tpl=('*','','')
res=any(tpl)
print(res)
#output: True

tpl=(' ',' ',' ')
res=any(tpl)
print(res)
#output: True

#------------ Check if all items in a Set are True:----------------
myset = {0, True, True}
res = any(myset)
print(res)
#output: True

#------------ Check if all items in a Dictionary are True:----------------
#When used on a dictionary, the all() function checks if all the keys are true, not the values.
dct = {0:'Apple', 1:'Boy', 2:3,3:[1,2,3]}
res = any(dct)
print(res)
#output: True

dct = {1:'Apple', 2:'Boy', 3:3,4:[1,2,3]}
res = any(dct)
print(res)
#output: True