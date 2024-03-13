# Write a Python script that asks the user for a temperature degree in Celsius, converts this value
# to the corresponding degree in Fahrenheit, and prints out the converted result

# Get input from user. 
# Specify its type as float by parsing the return value of input function with float() to let the python interpreter know that the input type is float number.
celcius = float(input("Type Celcius value: "))

# Calculate the Fahrenheit value with the releated formula.
fahrenheit = 1.8 * celcius + 32

# Print the result. 
# Make sure that you parse the float values by str() since you want to use string concatenation.
print(str(celcius) + " Celcius is equal to " + str(fahrenheit) + " Fahrenheit.")
