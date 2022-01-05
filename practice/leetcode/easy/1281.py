class Solution:
    def product(self, num):
        pro = 1
        while num != 0:
            x = num % 10
            pro *= x
            num //= 10
        return pro

    def sumDig(self, num):
        sm = 0
        while num != 0:
            x = num % 10
            sm += x
            num //= 10
        return sm

    def subtractProductAndSum(self, n):
        return self.product(n) - self.sumDig(n)