def imageSmoother(M):

    R, C = len(M), len(M[0])
    ans = [[0]*C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            value = 0
            size = 0

            for nr in [r-1, r, r+1]:
                for nc in [c-1, c, c+1]:
                    if 0 <= nr < R and 0 <= nc < C:
                        value += M[nr][nc]
                        size += 1
                    else:
                        value += 0
                        size += 1

            ans[r][c] = value/size

    return ans



# M = [[1, 1, 1, 1, 1],
#      [1, 1, 1, 1, 1],
#      [1, 1, 0, 1, 1],
#      [1, 1, 1, 1, 1],
#      [1, 1, 1, 1, 1]]

M = [[2,3,4],
     [5,6,7],
     [8,9,10],
     [11,12,13],
     [14,15,16]]

M_new = imageSmoother(M)
print (M_new)