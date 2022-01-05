from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1, s2):
        ls1 = s1.split(" ")
        ls2 = s2.split(" ")
        ls = ls1 + ls2
        mp = Counter(ls)
        res = list()
        for key, val in mp.items():
            if val == 1:
                res.append(key)
        return res
