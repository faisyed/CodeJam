class Solution:
    def singleNumber(self, nums):
        x = nums[0]
        for i in range(1, len(nums)):
            x^=nums[i]
        return x