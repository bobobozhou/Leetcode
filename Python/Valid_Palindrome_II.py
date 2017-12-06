def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    def isPalindrome(s_in, start, end, delCount):

        if delCount > 1:
            return False

        while start < end:
            if s_in[start] != s_in[end]:
                break

            start += 1
            end -= 1

        if start == end or start == end + 1:
            return True

        return any([isPalindrome(s_in, start+1, end, delCount + 1), isPalindrome(s_in, start, end - 1, delCount + 1)])


    s = list(s)
    return isPalindrome(s, 0, len(s) - 1, 0)



a = "abc"
print(validPalindrome(a))
