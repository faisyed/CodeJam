class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mx = nums[0]
        mn = nums[0]
        for i in range(1, len(nums)):
            if nums[i]<0:
                mx,mn = mn,mx
            mx = max(mx*nums[i],nums[i])
            mn = min(mn*nums[i],nums[i])
            if mx>res:
                res=mx
        return res