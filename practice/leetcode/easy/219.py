class Solution:
    def containsNearbyDuplicate(self, nums, k):
        mp = {}
        for ind, val in enumerate(nums):
            if val not in mp:
                mp[val] = ind
            else:
                if abs(ind - mp[val]) <= k:
                    return True
                else:
                    mp[val] = ind
        return False