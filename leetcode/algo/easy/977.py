class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        res = [0]*sz
        l = 0
        r = sz-1
        for i in range(sz-1,-1,-1):
            if abs(nums[l])<abs(nums[r]):
                res[i] = nums[r]**2
                r-=1
            else:
                res[i] = nums[l]**2
                l+=1
        return res