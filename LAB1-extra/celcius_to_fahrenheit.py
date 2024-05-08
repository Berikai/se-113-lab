# Exercise:
# Write a program which prompts the user to enter a Celsius temperature value and convert the temperature to Fahrenheit. 
# Print out the converted temperature.

# Get input from user. 
# Specify its type as float by parsing the return value of input function with float() to let the python interpreter know that the input type is float number.
celcius = float(input("Type Celcius value: "))

# Calculate the Fahrenheit value with the releated formula.
fahrenheit = celcius * 9 / 5 + 32

# Print the result. 
# Make sure that you parse the float values by str() since you want to use string concatenation.
print(str(celcius) + " Celcius is equal to " + str(fahrenheit) + " Fahrenheit.")
