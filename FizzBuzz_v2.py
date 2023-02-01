
def fizzbuzz(num1: int, num2: int) -> float:
    counter = 1
    while counter < 100:
        if counter % num1 == 0 and counter % num2 == 0:
            print("FizzBuzz")
        elif counter % num2 == 0:
            print('Buzz')
        elif counter % num1 == 0:
            print("Fizz")
        else:
            print(counter)
        counter += 1

fizzbuzz(3, 5)
