class Solution:
    def numIdenticalPairs(self, nums):
        sm = 0
        hm = {}
        for ind, val in enumerate(nums):
            if val not in hm:
                hm[val] = set((ind,))
            else:
                sm+=len(hm[val])
                hm[val].add(ind)
        return sm