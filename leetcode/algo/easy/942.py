class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l,h = 0, len(s)
        res = []
        for ch in s:
            if ch == 'I':
                res.append(l)
                l+=1
            else:
                res.append(h)
                h-=1
        res.append(l)
        return res