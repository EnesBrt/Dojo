# Detect Pangram

import string


def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(s.lower()))


phrase = "The quick brown fox jumps over the lazy dog"
resultat = is_pangram(phrase)
print(resultat)
