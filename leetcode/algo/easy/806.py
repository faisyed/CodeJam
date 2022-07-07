import string
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:        
        lw = string.ascii_lowercase
        mp = {}
        for w,ch in zip(widths, lw):
            mp[ch] = w
        cur = 0
        ln = 1
        for ch in s:
            req = mp[ch]
            if cur+req<=100:
                cur+=req
            else:
                ln+=1
                cur = req
        return [ln, cur]