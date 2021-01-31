# var1 is in the global namespace
var1 = 5
def some_func():
    # var2 is in the local namespace
    var2 = 6
    def some_inner_func():

        # var3 is in the nested local
        # namespace
        var3 = 7

# Python program processing
# global variable
count = 5
def some_method():
    global count
    count = count + 1
    print(count)
    some_method()

# python program showing
# a scope of object
def some some_func():
 print("Inside some func")
 def some_inner_func():
     var = 10
     print("inside inner function, value of var:",var)
     some_inner_func()
     print("Try printing var from outer function: ",var)
     some_func()


# Statement, Indentation and Comment in Python
 # python program showing
 # identation
 site = 'gfg'

 if site == 'gfg':
     print('Logging on to vipul dubey..')
 else:
     print('retype the URL.')
     print('All set !')

j = 1
while(j<= 5):
    print(j)
    j = j + 1

# This is a comment
# print "vipuldubey !" to console
print("vipuldubey")

a, b = 1, # Declaring two integers
sum = a + b # adding two inteers
print(sum) # displaying the output

""""
This would be a multiline comment in python that spans 
several lines and describes vipuldubey.
...
"""
print("vipuldubey")

"""
This article on vipuldubey gives you a perfect example 
of multi-line comments
"""
print("vipuldubey")


# Structuring Python Programs
print('Welcome to vipul dubey')

# Example 2
x = [1,2,3,4]

# x[1:3] means that start from the index
# 1 and go upto the index 2
print(x[1:3])

"""
in the above mentoned format,
the first index is included, but the 
last index is not included.
"""

# Example
a = 10; b = 20; c = b + a
print(a); print(b); print(c)

# Implicit Line Continuation
# Example 1
# The following code is valid
a = [
    [1,2,3],
    [3,4,5],
    [5,6,7]
]
print(a)

# Example 2
# The following code is also valid

person_1 = 18
person_2 = 20
person_3 = 12

 if(
     person_1 >= 18 and
     person_2 >= 18 and
     person_3 < 18
 ):
     print('2 persons should have ID cards')


# Explicit Line Continuation
# Example
x = \
    1 + 2 \
    + 5 + 6 \
    + 10
print(x)

# Example 2
""" This example will demonstrate
multiple comments
"""
""" The following
a variable contains the string
 'How old are you?
"""
a = 'How old are you?'
"""
The following statement prints what's
inside the variable a
"""
print(a)

# Example
""" The following statement prints the string 
stored in the variable
"""
a = 'This is # not a comment #'
print(a)

# Example
""" The following statement
prints the string stored
in the variable
"""
a = 'This is # not a comment #'
print(a) # prints the string stored in a

# Example 1
# This is correct
# Whitespace here can improve readability.
x = 10
flag =(x == 10)and(x<12)
print(flag)

""" Readable from could be as follows
x = 10
flag = (x ==10)and (x <12)
print(flag)
"""
# Try the more readable code yourself

# Example
x = [1,2,3]
y = 2
""" Following is incorrect , and will generate syntax error
a = yin x 
"""
# Corrected version is Written as
a = y in x
print(a)

