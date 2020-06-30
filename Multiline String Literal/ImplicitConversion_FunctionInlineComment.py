# File: ImplicitConversion_FunctionInlineComment.py
# This topic is covered under Multiline statement
# Implicit conversion between physical and logical lines support inline comments.


# Inline comment in function 

def my_func(arg_int, #first argument of Integer type
arg_str #second argument of string type
,arg_float #second argument of string type)
):
 print (str(arg_int)+arg_str+str(arg_float))


my_func(10,"ten",10.0)


#output:- 10ten10.0
