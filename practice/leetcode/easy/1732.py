class Solution:
    def largestAltitude(self, gain):
        res = list()
        res.append(0)
        mx = 0
        for i in range(len(gain)):
            val = res[i]+gain[i]
            if val>mx:
                mx = val
            res.append(val)
        return mx

"""
from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ls = [0] + list(accumulate(gain))
        return max(ls)
"""