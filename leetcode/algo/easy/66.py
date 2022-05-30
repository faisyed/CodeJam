class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        car = 1
        for i in range(len(digits)-1,-1,-1):
            sm = digits[i]+car
            res.append(sm%10)
            car = sm//10
        if car==1:
            res.append(1)
        return res[::-1]