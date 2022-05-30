class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n1 = 0
        for v in num:
            n1 = (n1*10)+v
        sm = n1+k
        res = []
        while sm!=0:
            res.append(sm%10)
            sm//=10
        return res[::-1]