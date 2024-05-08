# Modify your script for Question#2 by adding the following function: search_letter 
 
# search_letter - This function takes two strings and returns a bool value (i.e., either True or False). 
# The first argument value will be the source string to be searched and the second argument value will be the 
# key letter to be searched in the source. If the key letter is found in the source the function will return True, 
# otherwise False. 
 
# Test your search_letter function in the following way: Call the function by passing the final version 
# of the password created in Question#2 as the first argument value and your name’s first letter as the second 
# argument value. Check the function’s return value to see the result.  
 
# Note: This last task is just an illustration of using many different functions in a script. Using such a function 
# would not make sense in choosing strong passwords. Consider using different mechanisms to create strong 
# passwords. 

def search_letter(source, key_letter):
    if source.find(key_letter) != -1:
        return True
    else:
        return False
    
# 2.py code
import random

def rep_with_upper(string):
    random_index = random.randint(0, len(string) - 1)
    string = string[:random_index] + string[random_index].upper() + string[random_index + 1:]
    return string

def swap_letters(string):
    string = string[-2:] + string[2:-2] + string[:2]
    return string

# 1.py code
user_number = int(input('Enter a number between 3 and 7: '))
if not 3 <= user_number <= 7:
    print('Invalid number')
    exit()

many_words = open('../week12-lab/wordlist.10000')
many_words = many_words.read()
many_words_list = many_words.split()

chosen_words = []
for _ in range(user_number):
    random_number = random.randint(0, len(many_words_list) - 1)
    chosen_words.append(many_words_list[random_number])

password = ''
for word in chosen_words:
    password += word

password = rep_with_upper(password)
password = swap_letters(password)
print('Password:', password)

# Homework part
name = 'berkay'
print('Search result:', search_letter(password, name[0]))