# File: ImplicitConversion_ListInlineComment.py
# This topic is covered under Multiline statement
# Implicit conversion between physical and logical lines support inline comments.


# Inline comment in list literal
lst = [1 #first element of list lst
	 ,2 #second element of list lst
	 ,3 #third element of list lst
	 ]
print(lst)

#output:- [1, 2, 3]
