from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = Counter(nums)
        return max(mp.keys(), key=mp.get)