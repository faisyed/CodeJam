class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff = abs(nums[0])
        res = nums[0]
        for i in range(1,len(nums)):
            n = abs(nums[i])
            if n<diff:
                res = nums[i]
                diff = n
            elif n==diff:
                res = max(res, nums[i])
            else:
                continue
        return res