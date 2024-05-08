# Ask the user to enter 10 integers. Then, print the sum of the positive integers given. If the
# user enters a negative integer, it will not be added to the result.

sum = 0

for _ in range(10):
    number = int(input('Enter an integer: '))

    if number > 0:
        sum += number

print('Sum of the positive integers: ', sum)