from heapq import heapify, heappop


class Solution:
    def sortArray(self, nums):
        heapify(nums)
        return [heappop(nums) for i in range(len(nums))]
