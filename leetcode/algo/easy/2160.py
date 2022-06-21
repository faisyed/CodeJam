class Solution:
    def minimumSum(self, num: int) -> int:
        res = []
        while num!=0:
            x = num%10
            res.append(x)
            num//=10
        res.sort()
        n1 = res[0]*10+res[3]
        n2 = res[1]*10+res[2]
        return n1+n2