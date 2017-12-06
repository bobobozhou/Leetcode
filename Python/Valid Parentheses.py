def isValid(s):

    dict = {'(':')', '[':']', '{':'}'}
    stack = []

    for c in s:
        if c in dict:
            stack.append(c)

        else:
            if not stack or dict[stack.pop()] != c:
                return False

    return not stack

list = "()[]"
print (isValid(list))