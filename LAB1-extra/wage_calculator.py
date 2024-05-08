# Exercise:
# Write a program to prompt the user to enter hours and a rate per hour to compute a worker's wage.

# Note: The "\n" special character inserts new line in strings.

# Get work hours of the worker.
# Specify its type as float by parsing the return value of input function with float() to let the python interpreter know that the input type is float number.
hours = float(input("How many hours do you work?\n"))

# Get earning rate per hour of the worker.
# Specify its type as float by parsing the return value of input function with float() to let the python interpreter know that the input type is float number.
rate = float(input("How much money you earn per hour?\n"))

# Calculate the wage.
wage = hours * rate

# Print the result. 
# Make sure that you parse the float value by str() since you want to use it in string concatenation.
print("Your wage is " + str(wage) + " units of money.")