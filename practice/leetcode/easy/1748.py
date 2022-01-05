from collections import Counter
class Solution:
    def sumOfUnique(self, nums):
        mp = Counter(nums)
        sm = 0
        for key, val in mp.items():
            if val==1:
                sm+=key
        return sm