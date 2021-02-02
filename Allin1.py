# Instead of writing this massive Python code
# we can also code this in a different way

# Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword
import keyword

# initializing strings for testing while putting them in an array
keys = ["for", "while", "tanisha", "break", "sky",
        "elif", "assert", "pulkit", "lambda", "else", "sakshar"]

for i in range(len(keys)):
    # checking which are keywords
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword")
    else:
        print(keys[i] + " is not a python keyword")

        # python code to demonstrate working of is keyword()
        # importing "keyword" for keyword operations
        import keyword

        # printing all keywords at once using "kwlist()"
        print("The list of keywords is : ")
        print(keyword.kwlist)

    # python 3 code to demostrate variable assignment
    # upon condition using direct initialisation methd
    # initialising variable directly
    a = 5
    # printing value of a
    print("The value of a is: " + str(a))

    # One liner if-else instead of Conditional Operator (?:) in Python
    # Python 3 code to demostrate variable assignment
    # upon condition using one liner if-else
    # initialising variable using conditional operator
    # a = 20 > 10 ? : 0 is not possible in python
    a = 1 if 20 > 10 else 0

    # printing value of a
    print("The value of a is: " + str(a))

    # Print without newline in Python?
    print("vipul", end = " ")
    print("vipuldubey")

    # array
    a = [1, 2,3,4]
    # printing a element in same
    # line
    for i in range (4):
        print(a[i], end = " ")

    # python program to illustrate if statement
    #!/usr/bin/python
i = 20;
if (i < 15):
    print ("i is smaller than 15")
    print ("i'm in if Block")
else:
    print ("i is greater than 15")
    print ("i'm in else Block")
print ("i'm not in if and not in else Block")

# python program to illustrate nested if statement
# !/usr/bin/python
i = 10
if(i ==10):
    if(i < 15):
        print("i is smallert than 15")
# Nested- if ststement
# will only be executed if statement above
# it is true
if(i < 12):
    print("i is smaller than 12 too")
else:
    print("i is greater than 15")


# python program to illustrate if-else-else ladder
# !/usr/bin/python
i= 20
if(i==10):
    print("i is 10")
elif(i == 15):
    print("i is 15")
elif(i ==20):
    print("i is 20")
else:
    print("i is not present")

# python program to illustrate short hand if-else
i =10
print(True) if i < 15 else print(False)

# Basic calculator program using Python
# Python program for simple calculator
# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))
else:
    print("Invalid input")


# python to check input
# type in python
num = input("Enter number :")
print(num)
name1 = input("Enter name :")
print(name1)
# printing type of input value
print("type of nu,ber", type(num))
print("type of name", type(name1))

# Taking multiple inputs from user in Python
# python program showing how to
# multiple input using split
# taking two inputs at a time
x, y = input("Ener a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking two inputs at a time
a, b = input("Enter a two value: ").spilt()
print("First number is {} and second number is {}". format (a, b))
print()

# taking miltipile input at a time
# and type casting using list() function
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)

# python program showing
# how to take multiple input
# using list comprehension
# taking two input at a time
x, y = [int(x) for x in input("Enter three value").split()]
print("first number is: ", x)
print("Second Number is: ", y)
print()

# taking three input at a time
x, y, z =[int(x) for x in input("Enter three value: ").split()]
print("First Number is: ", x)
print("Second number is: ", y)
print("Third Number is: ", z)
print()

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First number is {} and second number is {}".format(x, y))
print()

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)