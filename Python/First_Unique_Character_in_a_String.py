def firstUniqChar(s):

    cha = 'abcdefghijklmnopqrstuvwxyz'

    index = [s.index(l) for l in cha if s.count(l) == 1]

    return min(index) if len(index) > 0 else -1


s = 'lleetcode'
print (firstUniqChar(s))
