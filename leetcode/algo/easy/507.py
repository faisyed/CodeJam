class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=0:
            return False
        res = 0
        i = 1
        while i*i<=num:
            if num%i==0:
                res+=i
                if i*i!=num:
                    res+=num//i
            i+=1
        return res-num==num