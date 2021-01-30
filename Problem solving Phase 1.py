# keywords in python set-1
print(False == 0)
print(True == 1)
print(True + True + True)
print(False + False + False)

# Python code to demonstrate
# True, False, None, and or not
# showing that None is not equql to 0
# prints False as its false.
print(None == 0)
# showing objetive of None
# here x and y both are null
# hence true
x = None
y = None
print(x == y)

# showing logical operation
# or (returns True)
print(True or False)
# showing logical operation
# and (returns False)
print(False and True)

# showing logical operation
# not (returns False)
print(not True)

# Python code to demonstrate
# del and assert
# initialising list
a = [1,2,3]

#printing list before deleting any value
print("The list before deleting any value")
print(a)

#using del to delete 2nd element of list
del a[1]
# printing list after deleting 2nd element
print("The list after deleting 2nd element")
print(a)

# demonstrating use of assert
# prints AseerrtionError
assert 5 < 3, "5 is not smaller than 3"

# Python code to demonstrate working of
# in and is
# using "in" to check
if 's' in 'vipul dubey':
    print("s is part of vipul dubey")
else: print("s is not part vipul dubey")

# using "in" to loop through
for i in 'vipuldubey':
    print(i,end=" ")
    print("\r")

# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')

# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memeory location
print({} is {})

# Python code to demonstrate working of
# global and non local
# initializing variable globally
a = 10
# used to read the variable
def read():
    print(a)

# changing the value of globally defined variable
def mod1 ():
    global a
    a = 5

# changing value of only local variable
def mod2():
    a = 15

# reading initial value of a
# prints 10
read()

# calling mod 1 function to modify value
# modifies value of global a to 5
mod()

# reading modified value
# prints 5
read()
# calling mod 2 function to modify value
# modifies value of local a to 15, doesn't effect gobal value
mod2()
# reading modified value
# again prints 5
read()
# demonstrate non local
# inner loop changing the value of outer a
# prints 10
print("Value of a using nonlocal is: ",end="")
def outer():
    a = 5
    def innner ():
        nonlocal a
        a = 10
        inner()
        print(a)

        outer()

# demonstrating withot using nonlocal
# inner loop not changing the value of outer a
# prints 5
print("Value of a without using nonlocal is : ",end="")
def outer():
    a = 10
    inner()
    print(a)
    outer()