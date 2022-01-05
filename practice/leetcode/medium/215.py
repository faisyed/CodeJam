from heapq import nlargest
class Solution:
    def findKthLargest(self, nums, k):
        res = nlargest(k, nums)
        return res[-1]