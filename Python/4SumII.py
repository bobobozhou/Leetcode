class Solution(object):
    def fourSumCount(self, A, B, C, D):

        import collections

        s_AB = collections.Counter(a + b for a in A for b in B)
        s = sum(s_AB[-c - d] for c in C for d in D)
        return s

A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]

K = Solution()
print (K.fourSumCount(A, B, C, D))

