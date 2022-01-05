from collections import Counter
class Solution:
    def majorityElement(self, nums):
        mp = Counter(nums)
        return max(mp, key=mp.get)