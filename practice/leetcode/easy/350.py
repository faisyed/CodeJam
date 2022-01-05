from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        mp1 = Counter(nums1)
        mp2 = Counter(nums2)
        mp = mp1 & mp2
        return mp.elements()