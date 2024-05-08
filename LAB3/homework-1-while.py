# Write a Python script that reads an integer from the user and prints out its factorial. (Do not use a
# function, use a loop)

# This example uses while loop

integer = int(input("Enter a number to calculate factorial: "))

factorial = 1

increment = 1

while increment <= integer:
    factorial *= increment
    increment += 1

print(f"{integer}! is", factorial)