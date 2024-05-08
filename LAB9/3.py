# In this last question, add your code the following: Open a file named “store.txt” in write mode. 
# Write your last password from the previous question. The file should have only one line, which is the 
# password you have generated. 

# Previous codes
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

# 3rd part starts here
store = open('store.txt', 'w')
store.write(password)
