#Defining the function and passed 1 parameter stuff.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')     #calling the split function on the parameter stuff and assigning that value to words variable 
    return words                #define words. Or this entire functions is supposed to return words when initiated.

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in full sentences and returns sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words and then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

