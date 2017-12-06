def isAnagram(s, t):

    # s_sorted = sorted(s)
    # t_sorted = sorted(t)
    #
    # return s_sorted == t_sorted

    dic1 = {}
    dic2 = {}

    for element in s:
        dic1[element] = dic1.get(element, 0) + 1

    for element in t:
        dic2[element] = dic2.get(element, 0) + 1

    return dic1 == dic2


a = 'cat'
b = 'act'
print isAnagram(a, b)

