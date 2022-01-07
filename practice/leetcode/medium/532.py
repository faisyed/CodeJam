from collections import Counter
class Solution:
    def findPairs(self, nums, k):
        mp = Counter(nums)
        res = 0
        for key in mp:
            if k>0 and key+k in mp:
                res+=1
            elif k==0 and mp[key] > 1:
                res += 1
        return res