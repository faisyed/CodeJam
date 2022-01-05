from collections import Counter
class Solution:
    def frequencySort(self, s):
        mp = Counter(s).most_common()
        res = ""
        for char, freq in mp:
            res += char*freq
        return res