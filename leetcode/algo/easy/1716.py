class Solution:
    def sumSeries(self, a, n=7):
        sm = (n*(2*a+(n-1)))//2
        return sm
    
    def totalMoney(self, n: int) -> int:
        prev_m = 1
        i = 1
        cur = 0
        while i+6<=n:
            cur+=self.sumSeries(prev_m)
            prev_m+=1
            i+=7
        if i!=n+1:
            cur+=self.sumSeries(prev_m,n-i+1)
        return cur