from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp = Counter(nums)
        res = 0
        for k,v in mp.items():
            res+=(mp[k]*(mp[k]-1))//2
        return res