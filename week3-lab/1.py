# Define a variable name and ask the user to enter their name. Greet the user using their name,
# and ask the user for their height (in meters) and weight (in kilograms). Finally, calculate and
# print the user's BMI (Body-Mass-Index) using the following formula:

name = input('What is your name? ')

height = float(input(f'Hello {name}, what is your height in meters? '))
weight = float(input('What is your weight in kilograms? '))

bmi = weight / (height * height)

print(f'Your BMI is {bmi}')