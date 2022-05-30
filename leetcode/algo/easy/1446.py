class Solution:
    def maxPower(self, s: str) -> int:
        prev = s[0]
        cnt = 1
        res = 1
        for i in range(1,len(s)):
            if s[i]==prev:
                cnt+=1
            else:
                prev = s[i]
                cnt=1
            res = max(res,cnt)
        return res