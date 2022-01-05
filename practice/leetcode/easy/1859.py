class Solution:
    def sortSentence(self, s):
        mp = {}
        ls = s.split()
        for val in ls:
            pos = int(val[-1])
            mp[pos] = val[:-1]
        res = ""
        for i in range(1, 10):
            if i in mp:
                res+=mp[i]
                res+=" "
        return res[:-1]