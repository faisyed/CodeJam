class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        l = len(nums)
        sm = sum(nums)
        mn = min(nums)
        mx = max(nums)
        req_sm = l*(2*mn+(l-1))//2
        if mx-mn+1 == l == len(set(nums)):
            return True
        return False
            