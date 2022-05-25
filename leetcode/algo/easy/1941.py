from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mp = Counter(s)
        return max(mp.values()) == min(mp.values())