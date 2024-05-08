# Ex 2.
# Write program that prompts for a list of numbers as above and at the end, prints out both the
# maximum and minimum of the numbers instead of the average.

minimum = float('inf')
maximum = float('-inf')

while True:
    try:
        user_input = input('Enter a number: ')

        if user_input == 'done':
            break

        number = int(user_input)

        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    except:
        print('Invalid input')

print(maximum, minimum)