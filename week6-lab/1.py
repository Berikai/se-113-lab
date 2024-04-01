# Write a Python script that reads two integers, (i and j) from the user and displays the numbers
# between them in increasing order excluding i and j. Please do not forget to check which one of the
# given numbers is smaller, so that you can start from a small number. (If the difference between
# given numbers is smaller than 2, exit the program.)

i = int(input("Please enter the first number: "))
j = int(input("Please enter the second number: "))

if abs(i - j) < 2:
    print("Exiting...")
else:
    for k in range(min(i, j) + 1, max(i, j)):
        print(k, end=" ")
