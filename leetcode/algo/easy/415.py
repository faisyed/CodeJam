class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i,j = len(num1)-1,len(num2)-1
        car = 0
        while i>=0 or j>=0:
            v1 = int(num1[i]) if i>=0 else 0
            v2 = int(num2[j]) if j>=0 else 0
            i-=1
            j-=1
            sm = v1+v2+car
            res+=str(sm%10)
            car = sm//10
            
        if car>0:
            res+="1"
        return res[::-1]