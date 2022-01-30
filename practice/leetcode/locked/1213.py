from collections import Counter

class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        mp = Counter(arr1 + arr2 + arr3)
        res = []
        for key in mp:
            if mp[key] == 3:
                res.append(key)
        return res
