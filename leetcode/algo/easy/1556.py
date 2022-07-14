class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ""
        cnt = 0
        while n!=0:
            x = n%10
            cnt+=1
            res+=str(x)
            if cnt==3:
                res+="."
                cnt = 0
            n//=10
        if res=="":
            return "0"
        return res[::-1] if res[-1]!="." else res[-2::-1]