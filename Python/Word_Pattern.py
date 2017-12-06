def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """

    t = str.split()

    a = map(pattern.find, pattern)
    b = map(t.index, t)

    return a == b

print (wordPattern("abba", "dog cat cat dog"))
