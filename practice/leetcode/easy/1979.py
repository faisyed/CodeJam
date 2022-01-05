class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def findGCD(self, nums):
        mx, mn = -99999, 99999
        for num in nums:
            if num > mx:
                mx = num
            if num < mn:
                mn = num
        return self.gcd(mx, mn)

