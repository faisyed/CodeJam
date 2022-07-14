class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        mn = float('inf')
        for i,n in enumerate(nums):
            if i%10==nums[i]:
                return i
        return -1