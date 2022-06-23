class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mx = nums[k-1]-nums[0]
        mn = 1
        for i in range(k,len(nums)):
            t_diff = nums[i]-nums[mn]
            mx = min(mx, t_diff)
            mn+=1
        return mx