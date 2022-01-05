class Solution:
    def missingNumber(self, nums):
        x1 = nums[0]
        for i in range(1, len(nums)):
            x1^=nums[i]
        x2 = 0
        for i in range(1, len(nums)+1):
            x2^=i
        return x1^x2