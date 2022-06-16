class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        if n==0:
            return 0
        nums.append(0)
        nums.append(1)
        mx = max(nums[0],nums[1])
        for i in range(2, n+1):
            quo = i//2
            rem = i%2
            if rem==0:
                nums.append(nums[quo])
            else:
                nums.append(nums[quo]+nums[quo+1])
            mx = max(mx,nums[-1])
        return mx