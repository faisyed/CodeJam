class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        p,n = 0,1
        for v in nums:
            if v>0:
                res[p] = v
                p+=2
            else:
                res[n] = v
                n+=2
        return res