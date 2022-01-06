class Solution:
    def fib(self, n):
        if n<=1:
            return n
        cur = 0
        prev1 = 0
        prev2 = 1
        for i in range(2, n+1):
            cur = prev1+prev2
            prev1 = prev2
            prev2 = cur
        return cur