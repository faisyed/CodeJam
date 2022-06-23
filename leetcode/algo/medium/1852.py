from collections import Counter
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums[:k])
        cnt = len(mp)
        res = [cnt]
        for i in range(k,len(nums)):
            mp[nums[i-k]]-=1
            if mp[nums[i-k]] == 0:
                cnt -= 1
            if mp[nums[i]] == 0:
                cnt += 1
            mp[nums[i]]+=1
            res.append(cnt)
        return res