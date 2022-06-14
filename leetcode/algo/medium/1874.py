class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        sm = 0
        for a,b in zip(nums1,nums2):
            sm += a*b
        return sm