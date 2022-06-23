class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        a,b,c = s[0],s[1],s[2]
        cnt = 0
        for i in range(3, len(s)):
            if a!=b and b!=c and c!=a:
                cnt+=1
            a = b
            b = c
            c = s[i]
        if a !=b and b!=c and c!=a:
            cnt+=1
        return cnt