class Solution:
    def isEven(self, num):
        cnt = 0
        while num != 0:
            x = num % 10
            cnt += 1
            num //= 10
        return cnt % 2 == 0

    def findNumbers(self, nums):
        res = 0
        for num in nums:
            if self.isEven(num):
                res += 1
        return res