class Solution:
    def arraySign(self, nums):
        z,n = 0,0
        for num in nums:
            if num == 0:
                z = 1
                break
            elif num < 0:
                n += 1
        if z == 1:
            return 0
        elif n%2!=0:
            return -1
        return 1