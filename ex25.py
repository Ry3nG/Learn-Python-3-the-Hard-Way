def break_words(stuff):
    """this function will break up words for us.

    Args:
        stuff ([string]): [the string to break]
    """
    words = stuff.split(' ')
    return words


def sort_words(words):
    """this function will sort words

    Args:
        words ([string]): [the string to sort]
    """
    return sorted(words)


def print_first_word(words):
    """prints the first word after popping it off.

    Args:
        words ([list]): [the list you want to operate on]
    """
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """prints the last word after popping it off.

    Args:
        words ([list]): [the list you want to operate on]
    """
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words.

    Args:
        sentence ([string]): [the sentence to sort]
    """
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """takes in a full sentence and returns the sorted words.

    Args:
        sentence ([string]): [the sentence you want to operate on]
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """sorts the words then print the first and last one.

    Args:
        sentence ([string]): [the string you want to operate on]
    """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)