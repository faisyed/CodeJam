class Solution:
    def countGoodSubstrings(self, s):
        cnt = 0
        for i in range(len(s)-2):
            sub = s[i:i+3]
            st = set(sub)
            if len(st) == 3:
                cnt+=1
        return cnt