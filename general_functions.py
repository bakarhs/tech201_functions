# Function

# D R Y - Don't Repeat Yourself

# Creating a function

# def print_something():  # def = define
#     print("Something has been printed")

# print_something()

# Functions and arguments

# def print_something(print_string):
#     print(print_string)
#
# print_something("this is my variable")
#
# print_something("this is the second time i called this function")

# Naming arguments are very important as they can be confusing later on
# in java:
# public void print_string(String_text)

# def greetings(name):
#     print("Hello, my name is " + name)
#
# greetings("Luke")
# greetings("Flo")
# greetings("Belal")
# greetings("Bakar")

# The Return statement

# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2, 2))

# Default arguments

# def addition(int1=3, int2=2):
#     return(int1 + int2)
#
# print(addition())
# print(addition(10, 10))
# print(addition())

# def multi_args(*multiargs):
#     print(type(multiargs))

#     for arg in multiargs:
#         print(arg)

# multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Type Hints

# def greeting(name: str):
#     print("Hello, my name is " + name)
#
# greeting(24601)

# def division(num1: int, num2: int) -> float:
#     return num1 / num2
#
# print(division(9,3))
# print(type(division(9,3)))
#
# def division(num1: int = 6, num2: int = 3) -> float:
#     return num1 / num2
#
# print(division())
# print(type(division(9,3)))

# Function best practice

## Name your functions clearly using lowercase and underscores
## All arguments should be clear in their need and where possible include their expected type
## Remember the return statment or your function will return `None`
## Keep functions small to preserve readability and simplicity
## Use comments in your functions/methods to give instuctions on how to use them
## Consider using type hints to avoid type errors when you run your code






