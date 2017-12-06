def strStr(haystack, needle):

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

haystack = "aaaneedle"
needle = "nee"

print (strStr(haystack, needle))