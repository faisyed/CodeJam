class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        for i in range(len(nums2)):
            mp[nums2[i]] = i
        res = []
        for v in nums1:
            res.append(mp[v])
        return res