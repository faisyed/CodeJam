class Solution:
    def maxSubArray(self, nums):
        curMax = nums[0]
        mxRes = nums[0]
        for num in nums[1:]:
            curMax = max(num, curMax+num)
            mxRes = max(mxRes, curMax)
        return mxRes