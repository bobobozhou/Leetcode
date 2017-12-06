def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    return " ".join(i[::-1] for i in s.split())


print (reverseWords("Let's take LeetCode contest"))