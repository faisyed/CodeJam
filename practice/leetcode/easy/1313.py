class Solution:
    def decompressRLElist(self, nums):
        res = list()
        for i in range(0, len(nums), 2):
            tp = [nums[i+1]]*nums[i]
            res.extend(tp)
        return res