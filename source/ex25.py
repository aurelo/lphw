def break_words(sentence):
    """This function will break up words for us."""
    return sentence.split(' ')


def sort_words(words):
    return sorted(words)


def get_first_word(words):
    return words.pop(0)


def get_last_word(words):
    return words.pop(-1)


def sort_sentence(sentence):
    return sort_words(break_words(sentence))


def print_first_and_last(words):
    print "first:", get_first_word(words)
    print "last:", get_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_and_last(words)

