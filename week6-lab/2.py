# Write a Python script that reads an integer value from the user. This value will represent the
# temperature degree (in Celsius) for today. Depending on this temperature value your program
# should display a comment on the weather of the day. If given value is below 10, the program
# should say “It is a cold day.” If the given value is more than 30, it should say “It is hot!!”.
# Lastly, if the given number is in between, the program should say “It is a pleasant day...”. After
# completing this first part, modify and improve your script to make it read any number of values
# until the user enters -1000. If the user enters -1000, the program will immediately exit.


while True:
    value = int(input("Please enter the temperature: "))

    if value == -1000:
        print("Exiting the program...")
        break

    if value < 10: 
        print("It is a cold day.")
    elif value > 30:
        print("It is hot!!")
    else:
        print("It is a pleasent day...")
    