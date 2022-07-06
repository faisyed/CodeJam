class Solution:
    def calculate(self, mp, word):
        res = ""
        for ch in word:
            res+=mp[ch]
        return int(res)
    
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        lw = "abcdefghij"
        mp = {}
        for i,v in enumerate(lw):
            mp[v] = str(i)
        c1 = self.calculate(mp, firstWord)
        c2 = self.calculate(mp, secondWord)
        c3 = self.calculate(mp, targetWord)
        return c1+c2 == c3