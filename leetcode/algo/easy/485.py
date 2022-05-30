class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for i,v in enumerate(nums):
            if v==1:
                cnt+=1
            else:
                cnt = 0
            res = max(cnt,res)
        return res