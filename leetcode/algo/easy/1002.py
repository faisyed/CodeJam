from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mp = Counter(words[0])
        for i in range(1,len(words)):
            mp&=Counter(words[i])
        return list(mp.elements())