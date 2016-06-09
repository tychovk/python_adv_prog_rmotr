"""
Write a function, that receives the path to a text file that contains JUST ONE
word per line, and returns a dictionary with the counter of words starting with
each letter from 'a' to 'z'.

Example:
  counter_by_letter('words.txt')
  # {
    'a': 2,
    'b': 10,
    'c': 0,
    ...
    'z': 1
  }

"""
import string


def counter_by_letter(filepath):

    the_dict = {}
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        the_dict.update({letter: 0})
    with open(filepath, 'r') as f:
        for line in f:
            first_letter = line[0].lower()
            the_dict[first_letter] += 1
    return the_dict
