class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = [i]
            else:
                mp[nums[i]].append(i)
        cnt = 0
        for key,v in mp.items():
            for i in range(len(v)-1):
                for j in range(i+1,len(v)):
                    if (v[i]*v[j])%k == 0:
                        cnt+=1
        return cnt