from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        mp = Counter(nums)
        ms, tw = 0,0
        for i in range(1, len(nums)+1):
            if i in mp and mp[i]==2:
                tw = i
            elif i not in mp:
                ms = i
        return [tw, ms]