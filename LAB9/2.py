# Next, define the following two functions in your code: 
 
# rep_with_upper - This function takes a string as its only parameter and returns a new string value. 
# The function should create the new string value by replacing a character randomly chosen inside the 
# given parameter with its uppercase version (e.g. a --> A). In your modified script, you will call this 
# function by passing the password created in Question#1 as the argument value. 
 
# swap_letters - This function takes a string as its only parameter and returns a new string value. 
# The  function  should  create  the  new  string  value  by  swapping  the  first  two  characters  of  the  given 
# parameter with the ones in  the last two (e.g. Password --> rdsswoPa).  In your modified script,  you 
# will  call  this  function  by  passing  the  password  returned  from  rep_with_upper  function  as  the 
# argument value. 
 
# Now, modify your script for Question#1 in the following manner: Using your answer to Question#1, 
# create the initial password; then using this password as the argument value to the rep_with_upper 
# function  create  a  new  password;  finally  using  this  new  password  as  the  argument  value  to  the 
# swap_letters function create the final version of the password. Your modified script should print 
# both the initial and the final versions of the password created.

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

many_words = open('wordlist.10000')
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