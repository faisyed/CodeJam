class Solution:
    def xorOperation(self, n, start):
        nums = list()
        for i in range(n):
            nums.append(start + (2*i))
        res = nums[0]
        for i in range(1, n):
            res^=nums[i]
        return res