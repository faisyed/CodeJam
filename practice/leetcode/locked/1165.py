class Solution:
    def calculateTime(self, keyboard, word):
        mp = {}
        for ind,ch in enumerate(keyboard):
            mp[ch] = ind+1
        prev = 1
        res = 0
        for ch in word:
            res+=abs(mp[ch]-prev)
            prev = mp[ch]
        return res