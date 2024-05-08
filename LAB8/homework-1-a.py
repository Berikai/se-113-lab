# Define a function named print_words which takes a string as a parameter. The function
# should automatically detect and print every word found in the string on different lines. The
# words may be meaningless, but they must be separated from other words with a whitespace
# character (“space” on your keyboard).
# Test your function in the following way: Read a string input from the user and call this
# function by passing the user input as the argument value.

def print_words(string):
    for word in string.split():
        print(word)

string = input('Enter a sentence: ')
print_words(string)