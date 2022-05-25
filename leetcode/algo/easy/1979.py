class Solution:
    def gcd(self, mn, mx):
        if mn==0:
            return mx
        return self.gcd(mx%mn,mn)
    
    def findGCD(self, nums: List[int]) -> int:
        mx,mn = -9999, 9999
        for num in nums:
            mx = max(num,mx)
            mn = min(num,mn)
        return self.gcd(mn,mx)