def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    vals = [i for i in range(1, n ** 2 + 1)]

    matrix = [['']*n for _ in range(n)]

    i, j, di, dj = 0, 0, 0, 1

    for ind in range(n ** 2):
        matrix[i][j] = vals[ind]

        if matrix[(i + di) % n][(j + dj) % n] != '':
            di, dj = dj, -di

        i += di
        j += dj

    return matrix

print (generateMatrix(3))
