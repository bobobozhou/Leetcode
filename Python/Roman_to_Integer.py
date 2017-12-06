def romanToInt(s):

    map = {"M":1000, "D":500 ,"C":100 , "L":50 , "X":10, "V":5, "I":1}

    result = 0

    for i in range(len(s)):
        a = s[i]
        if i > 0 and map[s[i]] > map[s[i-1]]:
            result -= map[s[i-1]]
            result += map[s[i]] - map[s[i-1]]

        else:
            result += map[s[i]]

    return result


print (romanToInt('MCMXCVI'))