from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        mp = Counter(s)
        for ind, ch in enumerate(s):
            if mp[ch]==1:
                return ind
        return -1