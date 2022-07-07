from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)
        mp = dict(sorted(mp.items(), key=lambda x:x[0], reverse=True))
        mp = dict(sorted(mp.items(), key=lambda x:x[1]))
        res = []
        for k,v in mp.items():
            res.extend([k]*v)
        return res