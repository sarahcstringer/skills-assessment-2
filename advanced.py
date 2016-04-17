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

    values = char_count.values()

    top_char_values = [0]

    for num in values:
        if num > top_char_values[0]:
            top_char_values = [num]
        elif num == top_char_values[0]:
            top_char_values.append(num)

    top_char = set()

    for key, value in char_count.items():
        for num in top_char_values:
            if num == value:
                top_char.add(key)

    return sorted(list(top_char))


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

    word_length = {}

    for word in words:
        word_length[len(word)] = word_length.get(len(word), []) + [word]

    word_length_sort = []
    for key, value in word_length.items():
        word_length_sort.append((key, sorted(value)))

    return sorted(word_length_sort)


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
