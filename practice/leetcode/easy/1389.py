class Solution:
    def createTargetArray(self, nums, index):
        res = list()
        for i in range(len(index)):
            res.insert(index[i], nums[i])
        return res