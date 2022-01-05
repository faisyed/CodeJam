class Solution:
    def findMaxConsecutiveOnes(self, nums):
        mx = 0
        cnt = 0
        for val in nums:
            if val == 1:
                cnt += 1
            else:
                if cnt > mx:
                    mx = cnt
                cnt = 0
        if mx < cnt:
            mx = cnt
        return mx