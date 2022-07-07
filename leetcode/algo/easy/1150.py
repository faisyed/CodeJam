class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        mp = {}
        l = 0
        for n in nums:
            if n not in mp:
                mp[n] = 1
            else:
                mp[n] += 1
            l+=1
        return mp.get(target,0)>l//2