class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for ind, val in enumerate(nums):
            diff = target-val
            if diff in mp:
                return [ind, mp[diff]]
            mp[val] = ind