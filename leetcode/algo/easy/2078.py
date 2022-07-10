class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        for i in range(1,len(colors)):
            if colors[i]!=colors[0]:
                res = max(res, i)
            if colors[i]!=colors[len(colors)-1]:
                res = max(res, len(colors)-i-1)
        return res