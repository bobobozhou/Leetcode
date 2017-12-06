def countAndSay(n):
    s = '1'
    for _ in range(n-1):
        temp = ''
        count = 0
        let = s[0]

        for l in s:
            if l == let:
                count += 1

            elif l != let:
                temp += str(count) + let
                let = l
                count = 1

        temp += str(count) + let
        s = temp
    return s


print (countAndSay(4))