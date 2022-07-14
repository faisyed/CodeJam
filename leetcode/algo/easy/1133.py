from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        mp = Counter(nums)
        mx = float('-inf')
        for k,v in mp.items():
            if v==1:
                if mx<k:
                    mx = k
        return mx if mx!=float('-inf') else -1