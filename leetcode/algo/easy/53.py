class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmx = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            curmx = max(curmx+nums[i], nums[i])
            res = max(res, curmx)
        return res