def reverseBits(n):
    ans = 0
    for i in range(32):
        ans = ans << 1
        ans = ans | (n & 1)
        n = n >> 1

    return ans


a = 43261596
print (reverseBits(a))  #964176192
