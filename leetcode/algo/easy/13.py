class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = mp[s[0]]
        prev = mp[s[0]]
        for i in range(1,len(s)):
            v = mp[s[i]]
            if prev<v:
                v = v-prev
                res = res-prev+v
            else:
                res+=v
            prev = mp[s[i]]
        return res
            