class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sm = 0
        pr = 1
        while n!=0:
            x = n%10
            sm+=x
            pr*=x
            n//=10
        return pr-sm