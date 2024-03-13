# Write a Python script that reads an integer from the user and prints out its factorial. (Do not use a
# function, use a loop)

# This example uses for loop

integer = int(input("Enter a number to calculate factorial: "))

factorial = 1

for i in range(integer):
    factorial *= i+1

print(f"{integer}! is", factorial)