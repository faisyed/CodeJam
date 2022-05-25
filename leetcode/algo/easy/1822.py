class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p,n = 0,0
        for num in nums:
            if num==0:
                return 0
            elif num>0:
                p+=1
            else:
                n+=1
        return 1 if n%2==0 else -1