"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
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


    "hello Diana see Diana see too."
    new_dict = {}

    word = phrase.split()
       
    for index in range(len(word)-1):
        key = word[index]

        new_dict[key] = new_dict.get(key, 0) + 1


    return {new_dict}


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melons = { 'Watermelon': 2.95,
            'Cantaloupe': 2.50,
            'Musk': 3.25,
            'Christmas': 14.25
            }

    price = melons.get(melon_name)

    return price


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

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """


    new_dict = {}

    word_list = words.rstrip().split() # splits string into list of words


    for index in range(len(word_list)-1):
        key = len(word_list[index])

        if key not in new_dict:
            new_dict[key] = [word_list[index]]
        else: 
            new_dict[key].append(word_list[index])

            ###################
            # still need to figure out how to sort the values for every key in the dict


    # Had a lot of trouble appending the new words with same length to the existing dictionary value list... 


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
    man         matey
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

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    phrase = "my student is not a man"

    pirate_dict = {'sir':'matey', 
            'hotel':'fleabag inn', 
            'student':'swabbie', 
            'man': 'matey', 
            'professor': 'foul blaggart',
            'restaurant':'galley', 
            'your': 'yer',
            'excuse': 'arr',
            'students': 'swabbies', 
            'are': 'be', 
            'restroom':'head', 
            'my': 'me',
            'is': 'be'
            }

    list_words = phrase.rstrip().split()

    results = "{}".format(word)

    for word in list_words:
        if word in pirate_dict:
            value = pirate_dict[word]
            results = result.append(str(value)) ##################

    print result


    # result is not working
    # the value (tranlated word) can not be "appended" back to the string




    return ""


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      
    names = [bagon, baltoy, yamask, starly, nosepass, kalob, nicky]

    names[0]

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

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    


    names = ["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky"]


    #dict keys = first_letters and values = names starting with that letter
    first_letter_dict = {}

    for index in range(len(names)-1): 
        first_letter = names[index][0]

        if first_letter not in first_letter_dict:
            first_letter_dict[first_letter] = [names[index]]
        else:
            first_letter_dict[first_letter].append(names[index])


        #building dictionary with names as keys, and values as names that start with the last letter of the key
    next_name_dict = {}

    for index in range(len(names)-1): 
        if names[index] not in next_name_dict:
            last_letter = names[index][-1]

            #new dict will copy the values from first_letter_dict
            next_name_dict[names[index]] = first_letter_dict[last_letter]
            
        #we have created below dict: 
        #
        # baron : ['nosepass' , 'nicky']
        # baltoy : ['yamask']
        # yamask : ['kalob']
        # starly : ['yamask']
        # nosepass : ['starly']
        # kalob : ['bagon' , 'baltoy']
        # nicky : ['yamask']
    from random import choice
        
    word = choice(next_name_dict.keys())
    result = [word]

    while "word not in results": 
        if word in next_name_dict:
            random_value = choice(next_name_dict[word])
            result = result.append(random_value)
        else:
            break ###########################

        # have to find another way to end the while loop.
        # while Key hasn't been added to the result yet... how?

    print result





    return []

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


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
