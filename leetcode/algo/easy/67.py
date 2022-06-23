class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r1 = a[::-1]
        r2 = b[::-1]
        res = ""
        car = 0
        i,j = 0,0
        while i<len(r1) or j<len(r2):
            v1 = int(r1[i]) if i<len(r1) else 0
            v2 = int(r2[j]) if j<len(r2) else 0
            sm = v1+v2+car
            res+=str(sm%2)
            car = sm//2
            i+=1
            j+=1
        if car == 1:
            res+=str("1")
        return res[::-1]