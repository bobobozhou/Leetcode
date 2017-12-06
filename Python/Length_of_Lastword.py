def lengthOfLastWord(s):

    sn = s.split()

    if sn:
        s_last = sn[-1]
        return len(s_last)

    else:
        return 0


s = ' '
print (lengthOfLastWord(s))