class Solution:
    def buildArray(self, nums):
        res = list()
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res