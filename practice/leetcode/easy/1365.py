class Solution:
    def smallerNumbersThanCurrent(self, nums):
        cnt = [0]*102
        for num in nums:
            cnt[num+1]+=1
        for i in range(1,101):
            cnt[i]+=cnt[i-1]
        res = list()
        for num in nums:
            res.append(cnt[num])
        return res