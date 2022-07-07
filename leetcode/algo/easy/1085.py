class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        mn = float('inf')
        for v in nums:
            if v<mn:
                mn = v
        sm = 0
        while mn!=0:
            x= mn%10
            sm+=x
            mn//=10
        return 0 if sm%2 else 1