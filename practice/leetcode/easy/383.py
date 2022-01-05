from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        mp1 = Counter(ransomNote)
        mp2 = Counter(magazine)
        for key, val in mp1.items():
            avail = mp2[key]
            if val>avail:
                return False
        return True