def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    fir_row = not all(matrix[0])

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        for j in range(len(matrix)-1, -1, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if fir_row:
        matrix[0] = [0] * len(matrix[0])

    return matrix

print (setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
