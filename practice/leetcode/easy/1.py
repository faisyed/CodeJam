class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for ind,num in enumerate(nums):
            diff = target-num
            if diff in mp:
                return [ind, mp[diff]]
            else:
                mp[num] = ind