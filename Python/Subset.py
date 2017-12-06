# ## Bits Manipulation
#def subsets(nums):
#     l = len(nums)
#     ans = []
#
#     for b in range(1 << l):
#         solution = []
#
#         for j in range(l):
#             if b & (1 << j):
#                 solution.append(nums[j])
#
#         ans.append(solution)
#
#     return ans


## DFS Method
def subsets1(nums):
    nums = sorted(nums)
    res = []
    dfs(nums, 0, [], res)
    return res

def dfs(nums, index, path, res):
    res.append(path)

    for i in range(index, len(nums)):
        dfs(nums, i + 1, path + [nums[i]], res)



a = [1, 2, 3, 4]
print (subsets1(a))


