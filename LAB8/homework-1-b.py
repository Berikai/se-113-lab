# Improve print_words such that every word is stripped of punctuation marks. Before
# printing each word, check every character within a word to see if there are any punctuation
# marks (Check for exclamation and question marks, dots, commas, colons and semicolons).
# If so, remove them. Assume that the punctuation marks can only be at the end of each word.

import string

def print_words(sentence):
    for word in sentence.split():
        polished_word = word.translate(str.maketrans('', '', string.punctuation))
        print(polished_word)

sentence = input('Enter a sentence: ')
print_words(sentence)
