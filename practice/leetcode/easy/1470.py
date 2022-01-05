class Solution:
    def shuffle(self, nums, n):
        res = list()
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res