from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp1 = Counter(nums1)
        mp2 = Counter(nums2)
        mp1 &= mp2
        return mp1.elements()