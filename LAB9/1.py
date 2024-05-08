# In this lab you will write a Python script that will generate random passwords from the given list 
# variable many_words_list. Your script should start by assigning a variable user_number to a value 
# to be entered by the user. This number should be validated and must be between 3 and 7, inclusive. 
# This  value  would  refer  to  the  number  of  words  to  be  chosen  randomly  from  the  list  variable 
# many_words_list.  Depending  on  the  value  of  user_number,  your  code  should  randomly  choose 
# that number of words from the many_words_list. Lastly, your script should concatenate these words 
# into one string to create the password and print it on the screen. 
# Hint: You will need “random” to be imported. You are free to explore its methods.

import random

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

print('Password:', password)