class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""]*len(s)
        for ind,ch in zip(indices,s):
            res[ind]=ch
        return "".join(res)