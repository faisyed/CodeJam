class Solution:
    def findFinalValue(self, nums: List[int], orig: int) -> int:
        mp = {}
        for i,v in enumerate(nums):
            mp[v] = i
        
        while orig in mp:
            orig *= 2
        return orig