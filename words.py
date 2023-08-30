# 1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!
# 2. Turn that into a function, ***print_upper_words***. Test it out. (Don’t forget to add a docstring to your function!)
# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def capitalize(strings):
    '''convert strings in a list into all uppercase'''
    for word in strings:
        print(word.upper())

def print_upper_words(words):
    '''converts words that start with the letter e to uppercase, case insensitive'''
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())


def print_upper_words2(words, starts_with):
    '''converts words that start with a specific character to upper case
    
    variables are words and starts_with

    example: print_upper_words2(['happy','healthy','smile','pizza'],'h')
        prints: 'HAPPY','HEALTHY'

    '''
    for word in words:
        for char in starts_with:
            if char == word[0]:
                print(word.upper())

