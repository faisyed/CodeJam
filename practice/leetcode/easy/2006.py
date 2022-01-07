class Solution:
    def countKDifference(self, nums, k):
        mp = defaultdict(int)
        cnt = 0
        for num in nums:
            cnt += mp[num - k] + mp[num + k]
            mp[num] += 1
        return cnt
