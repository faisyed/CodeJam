class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,h = 0, len(nums)-1
        res = -1
        while l<h:
            sm = nums[l]+nums[h]
            if sm<k:
                res = max(res, sm)
                l += 1
            else:
                h -= 1
        return res