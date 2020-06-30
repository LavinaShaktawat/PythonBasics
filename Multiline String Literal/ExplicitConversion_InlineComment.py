# File: ExplicitConversion_InlineComment.py
# This topic is covered under Multiline statement
# Explicit conversion between physical and logical lines does not support inline comments , but we can use multiline statement using \backslash character for explicit conversion.


# Explicit physical to logical conversion Using \ in if statement 
a=10
b=20
c=30

if a > b \
and a > c \
and b > c:
	print('c is smallest with value '+ format(c))
else:
	print('c is not smallest one as it has value '+ format(c))


#output:- c is not smallest one as it has value 30
