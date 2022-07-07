class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tp = nums.copy()
        tp.sort()
        mp = {}
        for ind,v in enumerate(tp):
            if v not in mp:
                mp[v] = ind
            else:
                continue
        res = []
        for v in nums:
            res.append(mp[v])
        return res