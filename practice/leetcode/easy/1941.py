from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s):
        mp = Counter(s)
        val = mp[s[0]]
        for key,v in mp.items():
            if val!=v:
                return False
        return True