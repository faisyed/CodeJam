from collections import Counter
class Solution:
    def frequencySort(self, nums):
        # counting frequency of each val and getting it in form of most common
        mp = Counter(nums).most_common()
        # sorting in decreasing order based on key i.e val
        mp.sort(key = lambda x: x[0], reverse=True)
        # sorting in increasing based on frequency
        mp.sort(key = lambda x: x[1])
        res = list()
        for val, freq in mp:
            res.extend([val]*freq)
        return res