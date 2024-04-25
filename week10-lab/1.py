# Define a function my_function that takes an integer x as a parameter and decides if x 
# is an even or an odd number. The function returns no value. To test your function, read an 
# integer from the user and print out whether it is even or odd using the function. 

def my_function(x): 
    if x % 2 == 0:
        print(f'{x} is an even number.')
    else:
        print(f'{x} is an odd number.')

i = int(input('Enter a number to check whether it is even or odd: '))
my_function(i)