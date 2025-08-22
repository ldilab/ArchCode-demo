
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not isinstance(words, list):
        return None
    if not all(isinstance(x, str) for x in words):
        return None
    if not all(x.islower() or x == '' for x in words):
        return None
    if not all(x.isalpha() or x == '' for x in words):
        return None

    l = sorted(words, key = lambda x: (-len(set(x)), x))
    return l[0] if len(l) > 0 else ''
