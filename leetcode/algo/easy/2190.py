class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        mp = {}
        for i in range(len(nums)-1):
            if nums[i]==key:
                if nums[i+1] not in mp:
                    mp[nums[i+1]] = 1
                else:
                    mp[nums[i+1]] += 1
        ls = list(sorted(mp.items(),key=lambda x:x[1],reverse=True))
        return ls[0][0]