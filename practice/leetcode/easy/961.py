from collections import Counter


class Solution:
    def repeatedNTimes(self, nums):
        mp = Counter(nums)
        n = len(nums) // 2
        for key, val in mp.items():
            if val == n:
                return key
