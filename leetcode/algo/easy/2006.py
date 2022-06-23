from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        cnt = 0
        for i in range(len(nums)):
            cnt+=mp[nums[i]-k]+mp[nums[i]+k]
            mp[nums[i]]+=1
        return cnt