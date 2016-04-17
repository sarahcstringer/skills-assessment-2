"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    # using dictionary:
    # word_dictionary = {}
    # for word in words:
    #     word_dictionary[word] = word_dictionary.get(word, 1)

    # words = word_dictionary.keys()

    # return words

    # using sets:
    return list(set(words))




def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # use set math to find intersection of unique item
    union_items = set(items1) & set(items2)
    # return as a list
    return list(union_items)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # separate string into list of words
    phrase = phrase.split()

    # create empty dictionary
    word_count = {}

    # count words and store as key-value pairs in dictionary
    for word in phrase:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a boy")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a boy!")
        'me swabbie be not a boy!'
    """

    # note: updated Doctest b/c boy and man were changed in the Pirate dictionary

    # create dictionary
    pirate_talk = {
                'sir': 'matey',
                'hotel': 'fleabag inn',
                'student': 'swabbie',
                'boy': 'matey',
                'professor': 'foul blaggart',
                'restaurant': 'galley',
                'your': 'yer',
                'excuse': 'arr',
                'students': 'swabbies',
                'are': 'be',
                'restroom': 'head',
                'my': 'me',
                'is': 'be'}

    # split the phrase into individual words
    phrase = phrase.split()

    # loop through the list of words and check if word is in dictionary.
    # if yes, substitute that word with the Pirate word.
    for i, word in enumerate(phrase):
        if word in pirate_talk:
            # here I tried to do word = pirate_talk[word], but it didn't work
            # it only worked when I referenced the list index instead of the list
            # element itself
            phrase[i] = pirate_talk[word]

    # return the phrase as a string
    return " ".join(phrase)


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """

    word_lengths = {}

    sorted_word_lengths = []

    # store the length of each word as a key and the word itself as a list
    # for the value of that key
    for word in words:
        word_lengths[len(word)] = word_lengths.get(len(word), []) + [word]

    # get a list of tuples of key-value pairs from the dictionary
    for item, value in word_lengths.items():
        sorted_word_lengths.append((item, value))

    # return a sorted final list (dictionaries are unordered so the keys might
    # not be sorted when added to the list)
    return sorted(sorted_word_lengths)


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    
    numbers_neg = set()
    numbers_pos = set()

    # create a set of positive and a set of negative numbers in the list. Only
    # need absolute value of the number.
    for num in numbers:
        if num < 0:
            numbers_neg.add(abs(num))
        elif num > 0:
            numbers_pos.add(abs(num))
        # add zero to both lists
        elif num == 0:
            numbers_neg.add(num)
            numbers_pos.add(num)

    # find the union of the lists, which would mean the number and its negative
    # both appeared in the list of numbers
    pairs = list(numbers_neg & numbers_pos)

    return_pairs = []

    # create a list of the numbers and their negatives that appeared in the list
    for num in pairs:
        return_pairs.append([num, -num])

    return return_pairs



def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    words = {}
    # can only use each word once; pop items so that they're not reused
    word_chain = [names.pop(0)]

    # iterate through the list of names and create a dictionary
    # The key is the first letter of the word; values are the words that start
    # with that letter
    for name in names:
        words[name[0]] = words.get(name[0], []) + [name]
    
    # loop through and create a chain
    while True:
        # find the last letter of the last word in the chain
        last_letter = word_chain[-1][-1]
        # find the words that start with that letter and add the first one
        # to the list.
        if last_letter in words:
            word_chain.append(words.pop(last_letter)[0])
        else:
            return word_chain


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
