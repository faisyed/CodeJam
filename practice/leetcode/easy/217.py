class Solution:
    def containsDuplicate(self, nums):
        hm = {}
        for num in nums:
            if num in hm:
                return True
            else:
                hm[num] = 1
        return False
