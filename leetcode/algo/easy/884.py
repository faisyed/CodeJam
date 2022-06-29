from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1+ " " +s2
        mp = Counter(s.split())
        return [w for w in mp if mp[w]==1]