class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        l = len(s)
        for i in range(0,l,2):
            res+=s[i]
            if i+1<l:
                res+=chr(ord(s[i])+int(s[i+1]))
        return res