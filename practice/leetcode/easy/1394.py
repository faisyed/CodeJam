from collections import Counter
class Solution:
    def findLucky(self, arr):
        mp = Counter(arr)
        mx = -1
        for key,val in mp.items():
            if key==val and key>mx:
                mx = key
        return mx