# Define two variables number1 and number2. Then, ask the user to enter two real numbers
# for these variables. Then, using these two values, calculate and print the results of addition,
# subtraction, multiplication, division, exponentiation, remainder and quotient operations.

number1 = float(input("Enter 1st number: "))
number2 = float(input("Enter 2nd number: "))

sum = number1 + number2
diff = number1 - number2
prod = number1 * number2
div = number1 / number2
exp = number1 ** number2
rem = number1 % number2
quo = number1 // number2

print("Addition is %.1f" % sum)
print("Substraction is %.1f" % diff)
print("Multiplication is %.1f" % prod)
print("Division is %.1f" % div)
print("Exponentiation is %.1f" % exp)
print("Remainder is %.1f" % rem)
print("Quotient is %.1f" % quo)