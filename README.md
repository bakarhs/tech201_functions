# tech201_functions
tech201_functions

# Function
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

D R Y - Don't Repeat Yourself - The DRY or “Don't Repeat Yourself” principle is a software development practice aimed at reducing repetition of information.

# Creating a function
Example:
``` python
def print_something():  # def = define
    print("Something has been printed")

print_something()
```
Returns:
```
Something has been printed
```
# Functions and arguments
Example:
``` python
def print_something(print_string):
    print(print_string)

print_something("This is my variable")

print_something("This is the second time i called this function")
```
Returns:
``` 
This is my variable
This is the second time i called this function
```

Naming arguments are very important as they can be confusing later on
in java:
- Public void print_string(String_text)

``` python
def greetings(name):
    print("Hello, my name is " + name)

greetings("Luke")
greetings("Flo")
greetings("Belal")
greetings("Bakar")
```
Returns:
```
Hello, my name is Luke
Hello, my name is Flo
Hello, my name is Belal
Hello, my name is Bakar
```
## The Return statement
The Python return statement is a special statement that you can use inside a function or method to send the function's result back to the caller. A return statement consists of the return keyword followed by an optional return value. The return value of a Python function can be any Python object.

Example of using return:
``` python
def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))
```
Results:

```commandline
4
```
# Default arguments
Example:
``` python
def addition(int1=3, int2=2):
    return(int1 + int2)

print(addition())
print(addition(10, 10))
print(addition())
```
Returns:
```commandline
5
20
5
```
Example of multiple arguments:
``` python
def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

# Type Hints
Type hints are performed using Python annotations. They are used to add types to variables, parameters, function arguments as well as their return values, class attributes, and methods. Adding type hints has no runtime effect: these are only hints and are not enforced on their own

Example:
``` python
def greeting(name: str):
    print("Hello, my name is " + name)

greeting(24601)
```
This code will be invalid as the function is expecting string however, the user has inputted integers.

Example of how we should use hints:
```python
def division(num1: int, num2: int) -> float:
    return num1 / num2

print(division(9,3))
print(type(division(9,3)))

def division(num1: int = 6, num2: int = 3) -> float:
    return num1 / num2

print(division())
print(type(division(9,3)))
```
Results :
```commandline
3.0
<class 'float'>
2.0
<class 'float'>
```

# Function best practice
- Name your functions clearly using lowercase and underscores
- All arguments should be clear in their need and where possible include their expected type
- Remember the return statement or your function will return `None`
- Keep functions small to preserve readability and simplicity
- Use comments in your functions/methods to give instructions on how to use them
- Consider using type hints to avoid type errors when you run your code


# Using functions to create a simple calculator

The code I came used:
``` python
def calculator(operator, num1: float, num2: float) -> float:
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        print("Invalid")

print(calculator("+", 50, 50))
print(calculator("-", 100, 10))
print(calculator("*", 10, 8))
print(calculator("/", 81, 5))
```
1. I start of by making my function knowing that i will need 3 inputs. One for what operator is being used `"+", "-", "*", "/"`. The other 2 will be the numbers we use in our operation. also i want to note i specified these numbers are floats and left a hint that this function is using floats.
2. I begin to use an `if` statement this way I can do multiple operations in the same function. In this first if statement I am using is to make sure I can use addition `+` and " need to do this by specifying `if operator == "+":`
3. Now I need to specify the output of the if statement, I do thin with `return`. in my code i have written `return num1 + num2`, this is the output I need in order to add `num1` and `num2` together after writing the initial line of code `if operator == "+":`
4. This is then done for all the other operators: `-`,`*` and `/`, using an `elif` instead of `if` to keep it all part of the same code.
5. I end the function with an `else` statement incase the user inputs something I did not account for letting them know that their input was "Invalid"
6. You can then see bellow how I use this function whilst using `print()`