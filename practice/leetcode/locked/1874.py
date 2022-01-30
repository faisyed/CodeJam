class Solution:
    def minProductSum(self, nums1, nums2):
        mx = sorted(nums1,reverse=True)
        mn = sorted(nums2)
        res = 0
        for i in range(len(mx)):
            res+= mx[i]*mn[i]
        return res