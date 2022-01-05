class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = 0
        p2 = 0
        tp = nums1[:m]
        for i in range(m + n):
            if p2 >= n or (p1 < m and tp[p1] <= nums2[p2]):
                nums1[i] = tp[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
