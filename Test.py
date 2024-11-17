import Levenshtein

def levenshtein_similarity(address1, address2):
    return Levenshtein.ratio(address1.lower(), address2.lower())

address1 = "120 Main Street"
address2 = "123 Main Str."
print(levenshtein_similarity(address1, address2))  # Output: Similarity ratio

from fuzzywuzzy import fuzz

def fuzzy_match(address1, address2):
    return fuzz.ratio(address1.lower(), address2.lower())

print(fuzzy_match(address1, address2))  # Output: Similarity score


import difflib

def difflib_similarity(address1, address2):
    return difflib.SequenceMatcher(None, address1.lower(), address2.lower()).ratio()

print(difflib_similarity(address1, address2))  # Output: Similarity ratio
