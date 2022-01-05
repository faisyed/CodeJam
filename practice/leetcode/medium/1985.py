from heapq import nlargest
class Solution:
    def kthLargestNumber(self, nums, k):
        res = nlargest(k, [int(num) for num in nums])
        return str(res[-1])