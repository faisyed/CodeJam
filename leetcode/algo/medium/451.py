from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        mp = Counter(s)
        res = dict(sorted(mp.items(),key= lambda mp:mp[1], reverse=True))
        rs = ""
        for k,v in res.items():
            rs+=k*v
        return rs