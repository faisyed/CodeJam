class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        mf,mx = (0,nums[0]), (-1,-1)
        for i in range(1,len(nums)):
            if nums[i]>mf[1]:
                mx = mf
                mf = (i,nums[i])
            elif nums[i]>mx[1]:
                mx = (i,nums[i])
        if mf[1]>=mx[1]*2:
            return mf[0]
        return -1