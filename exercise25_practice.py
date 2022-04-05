def dismantle_sentence(sentence):
    words = sentence.split(" ")
    sort_words = sorted(words)
    first_word = sort_words.pop(0)
    last_word = sort_words.pop(-1)
    first_and_last_words = first_word + last_word
    
    print(words)
    print(sort_words)
    print(first_word)
    print(last_word)
    print(first_and_last_words)

    
dismantle_sentence("All good things come to those who wait.")
