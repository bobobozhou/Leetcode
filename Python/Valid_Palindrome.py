def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    lis = []
    for c in s:
        if c.isalnum():
            lis.append(c.lower())

    if lis == lis[::-1]:
        return True
    else:
        return False


s = 'A man, a plan, a canal: Panama'
print (isPalindrome(s))
