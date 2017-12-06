def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for _ in range(rowIndex):
        a = [0] + row
        b = row + [0]
        row = [sum(x) for x in zip(a, b)]

    return row


print (getRow(3))