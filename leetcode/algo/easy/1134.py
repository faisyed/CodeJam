class Solution:
    def isArmstrong(self, n: int) -> bool:
        l = len(str(n))
        tp = n
        res = 0
        while n!=0:
            x = n%10
            res+=x**l
            n//=10
        return tp==res