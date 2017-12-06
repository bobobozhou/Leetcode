def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in xrange(len(strs[0])):
        for string in strs[1:]:
            if i > len(string) or string[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]

m = ["my_prefix_what_ever",
     "my_prefix_what_so_ever",
     "my_prefix_doesnt_matter"]

# m = ["aaa"]

print (longestCommonPrefix(m))

