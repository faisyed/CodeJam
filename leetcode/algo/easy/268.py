class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r1 = 0
        for n in nums:
            r1^=n
        r2 = 0
        for i in range(len(nums)+1):
            r2^=i
        return r1^r2