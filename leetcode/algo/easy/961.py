from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mp = Counter(nums)
        l = len(nums)
        for k,v in mp.items():
            if v==l//2:
                return k