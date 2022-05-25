from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = Counter(s)
        for ch in t:
            if ch not in mp or mp[ch]==0:
                return ch
            else:
                mp[ch]-=1