# Improve your script in the following way: Add an exit option to the menu. If the user 
# enters 0, the program will immediately exit. Make the program run in a loop until the 
# user selects the exit option.  

import math

def is_even(x): 
    if x % 2 == 0:
        print(f'{x} is an even number.')
    else:
        print(f'{x} is an odd number.')

def sine_function(d):
    return math.sin(d * (math.pi/180))

def logarithm_function(b, n):
    return math.log(n, b)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        num1, num2, next = 0, 1, 2
        i = 1
        while i < n:
            next = num1 + num2
            num1, num2 = num2, next
            i += 1
        return next
    else:
        raise ValueError('Negative values are not allowed in def fibonacci(n):')

print("""
To decide whether a given number is even or odd, Enter 1.
To calculate sine of a given degree, Enter 2.
To calculate the logarithm of a given number, Enter 3.
To calculate the Fibonacci value for a given number, Enter 4.
To exit the program, Enter 0.
""")

while True:
    operation = int(input('Select an operation: '))
    print()

    if operation == 1:
        x = int(input('Enter a number to check whether it is even or odd: '))
        is_even(x)
    elif operation == 2:
        x = int(input('Enter a number in degrees to calculate the sine: '))
        print(f'Sine of {x} degree is {sine_function(x)}')
    elif operation == 3:
        x = int(input('Enter a number as base to calculate the logarithm: '))
        y = int(input('Enter a number to calculate the logarithm according to base: '))
        print(f'Logarithm of {x} is {logarithm_function(x, y)}')
    elif operation == 4:
        x = int(input('Enter a number to calculate Fibonacci value: '))
        print(f'Fibonacci value of {x} is {fibonacci(x)}')
    elif operation == 0:
        break
    else:
        print('Please give a number between 0 and 4')
    print()