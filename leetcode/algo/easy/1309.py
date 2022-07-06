import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        lw = string.ascii_lowercase
        mp = {}
        for i,v in enumerate(lw):
            mp[str(i+1)] = v
        res = ""
        i = len(s)-1
        while i>=0:
            if s[i] == "#":
                res+=mp[s[i-2:i]]
                i-=3
            else:
                res+=mp[s[i]]
                i-=1
        return res[::-1]