from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mp = Counter(nums)
        sm = 0
        for k,v in mp.items():
            if v==1:
                sm+=k
        return sm