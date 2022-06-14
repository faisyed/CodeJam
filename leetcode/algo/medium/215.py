import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ls = heapq.nlargest(k, nums)
        return ls[-1]