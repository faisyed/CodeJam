class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = -999999
        cur_sm = 0
        for i in range(k):
            cur_sm += nums[i]
        prev = 0
        avg = cur_sm/k
        mx = max(avg,mx)
        for i in range(k,len(nums)):
            cur_sm -= nums[prev]
            cur_sm +=nums[i]
            prev+=1
            avg = cur_sm/k
            mx = max(avg,mx)
        return mx