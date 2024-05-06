# Define a function occurrence that takes 2 parameters source_string and letter.
# The function should count and display the number of times letter appears in
# source_string. It shouldn’t return anything. The argument value to be passed to the
# parameter letter must be a single character, if it’s not, an error message should be
# given.
# Test your function by first getting an input string from the user, and then a letter to be
# searched within the string. Then, call the function occurrence by passing the input
# string and input character values as arguments.
# Note: The argument letter can be any character (including punctuation marks, numbers,
# whitespaces, etc.)

def occurence(source_string, letter):
    if len(letter) != 1:
        print('Invalid letter!')
    else:
        count = 0
        for i in source_string:
            if i == letter:
                count+=1
        print(f"The letter '{letter}' occurs in '{source_string}' {count} times. ")

string = input('Please enter a string to be searched: ')
letter = input('Please provide a letter to be searched for: ')

occurence(string, letter)


