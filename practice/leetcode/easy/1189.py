from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text):
        mp = Counter(text)
        bcnt = mp["b"]
        acnt = mp["a"]
        lcnt = mp["l"] // 2
        ocnt = mp["o"] // 2
        ncnt = mp["n"]
        return min(bcnt, acnt, lcnt, ocnt, ncnt)
