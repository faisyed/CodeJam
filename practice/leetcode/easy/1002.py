from collections import Counter
class Solution:
    def commonChars(self, words):
        mp = Counter(words[0])
        for word in words:
            mp1 = Counter(word)
            for key in mp.keys():
                mp[key] = min(mp[key],mp1[key])
        return mp.elements()

"""
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mp = Counter(words[0])
        for word in words:
            mp1 = Counter(word)
            mp = mp & mp1
        return mp.elements()
"""