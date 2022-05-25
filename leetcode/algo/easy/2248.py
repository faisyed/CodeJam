from collections import Counter

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        mp = Counter(nums[0])
        for i in range(1, len(nums)):
            mp&=Counter(nums[i])
        res = list(mp.elements())
        return sorted(res) 
        