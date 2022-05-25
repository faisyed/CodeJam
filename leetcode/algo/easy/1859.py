class Solution:
    def sortSentence(self, s: str) -> str:
        ls = s.split()
        mp = {}
        for w in ls:
            od = w[-1]
            mp[int(od)] = w[:-1]
        res = []
        for i in range(1, len(ls)+1):
            res.append(mp[i])
        return " ".join(res)