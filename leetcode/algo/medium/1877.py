class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mx = float('-inf')
        i,j = 0,len(nums)-1
        while i<j:
            sm = nums[i]+nums[j]
            mx = max(mx,sm)
            i+=1
            j-=1
        return mx