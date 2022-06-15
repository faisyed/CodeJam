class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mp = {}
        for ind,v in enumerate(keyboard):
            mp[v]=ind
        prev = keyboard[0]
        sm = 0
        for ch in word:
            sm+=abs(mp[prev]-mp[ch])
            prev = ch
        return sm