class Solution:
    def restoreString(self, s: str, indices):
        ls = [""]*len(s)
        for i in range(len(indices)):
            ls[indices[i]] = s[i]
        return "".join(ls)

"""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ls = [""]*len(s)
        for ind, ch in zip(indices, s):
            ls[ind] = ch
        return "".join(ls)
"""