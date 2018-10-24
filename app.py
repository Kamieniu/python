import random


class WordClass(object):
    def __init__(self, category=None, word=None):
        self.category = category
        self.word = word


array_of_words = []

array_of_words.append(WordClass('programming language', 'go lang'))
array_of_words.append(WordClass('programming language', 'python'))
array_of_words.append(WordClass('programming language', 'javascript'))
array_of_words.append(WordClass('programming language', 'php'))
array_of_words.append(WordClass('programming language', 'pascal'))
array_of_words.append(WordClass('programming language', 'scala'))

# Lenght of word array
# Returns Number
array_of_words_length = len(array_of_words)

# Get random number from 0 to number of items in array
random_number = int(random.uniform(0, array_of_words_length))

# Randomly chosen word
chosen_value = array_of_words[random_number]

chosen_word = chosen_value.word
chosen_category = chosen_value.category


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


# Check if given input is string (letter)


def insert_letters_to_array(index, letter):
    my_word[index] = letter
    print(my_word)


my_word = [''] * len(chosen_word)
strkies_counter = 3

print(f'Let\'s play \n Category: {chosen_category}')

while ''.join(my_word) != chosen_word or strkies_counter == 0:

    user_letter = input('Give me a letter: ')

    if user_letter.isalpha():

        found_letter_in_word_index = find(chosen_word, user_letter)

        if found_letter_in_word_index:

            for index in found_letter_in_word_index:

                insert_letters_to_array(index, user_letter)

        else:
            if strkies_counter == 0:
                print('You loose')
                break
            else:
                strkies_counter -= 1
                print(f'wrong! You have {strkies_counter} left!')

    else:
        print('Give me a letter!')

print('GREAT! The word is', chosen_word)
