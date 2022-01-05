class Solution:
    def sumZero(self, n: int):
        even = n%2==0
        res = list()
        hl = n//2
        if even:
            return [i for i in range(-hl,hl+1) if i!=0]
        else:
            return [i for i in range(-hl,hl+1)]