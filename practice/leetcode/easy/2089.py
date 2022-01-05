class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        res = list()
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res