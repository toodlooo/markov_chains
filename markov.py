from random import choice

from sys import argv


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi'): ['there']}
    """

    chains = {}
    splitted_text = text_string.split()

    for each_word in range(len(splitted_text) - 2):
        # Split text and added tuple keys to dictionary
        bi_gram = (splitted_text[each_word], splitted_text[each_word + 1])

        if bi_gram not in chains:
            # chains[bi_gram] = []
            # next_word = splitted_text[each_word + 2]
            # chains[bi_gram].append(next_word)
            chains[bi_gram] = [ splitted_text[each_word + 2] ]
        else:
            # next_word = splitted_text[each_word + 2]
            # chains[bi_gram].append(next_word)
            chains[bi_gram].append(splitted_text[each_word + 2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    for bi_gram, new_word in chains:
        new_key = ( bi_gram, choice(new_word) )
        print new_key
    return text





input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print chains

# Produce random text
random_text = make_text(chains)

print random_text
