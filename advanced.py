"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    # start an empty dictionary to keep a count of each character
    char_count = {}
    
    #loop through the string, removing spaces.
    for char in phrase.replace(' ',''):
        #add each string to the dictionary and increase count
        char_count[char] = char_count.get(char, 0) + 1

    # get the count of each key in the dictionary
    values = char_count.values()

    top_char_values = [0]

    # loop through the list of values. If a number in the list is greater than
    # the top_char_values character, set that to equal the new top_char_values.
    for num in values:
        if num > top_char_values[0]:
            top_char_values = [num]

    top_char = []

    # loop through the key-value pairs and find the characters that match the
    # top_char_values amount
    for key, value in char_count.items():
        for num in top_char_values:
            if num == value:
                top_char.append(key)

    return sorted(top_char)


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    # create empty dictionary
    word_length = {}

    # loop through the words in the list and create a key for each word length
    # and add the words of that length as values to the key.
    # If there are multiple words of the same length, store those as a list.
    for word in words:
        word_length[len(word)] = word_length.get(len(word), []) + [word]

    # create an empty list   
    word_length_sort = []

    # loop through the different key-value pairs in the dictionary and add them
    # to a list. Sort lists of multiple words alphabetically
    for key, value in word_length.items():
        word_length_sort.append((key, sorted(value)))

    # return a sorted list of tuples (sorted by word length)
    return sorted(word_length_sort)


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
