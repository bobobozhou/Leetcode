def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    if not matrix:
        return []

    i, j, di, dj = 0, 0, 0, 1
    ans = []
    r, c = len(matrix), len(matrix[0])

    for _ in range(r * c):

        ans. append(matrix[i][j])
        matrix[i][j] = ''

        if matrix[(i + di) % r][(j + dj) % c] == '':
            di, dj = dj, -di

        i += di
        j += dj

    return ans


print (spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
