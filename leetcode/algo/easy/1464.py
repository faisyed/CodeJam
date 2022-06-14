import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i,v in enumerate(nums):
            nums[i] = -1*v
        heapq.heapify(nums)
        n1,n2 = -1*heapq.heappop(nums), -1*heapq.heappop(nums)
        return (n1-1)*(n2-1)