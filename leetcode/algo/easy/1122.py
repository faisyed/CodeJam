from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = Counter(arr1)
        res = []
        for v in arr2:
            res.extend([v]*mp[v])
            mp.pop(v)
        ls = list(mp.elements())
        res.extend(sorted(ls))
        return res