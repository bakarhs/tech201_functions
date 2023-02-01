# using functions to build a calculator

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

# using functions to convert distances

def convert(num1: float, units) -> float:
    if units == "cm":
        return num1 * 10
    else