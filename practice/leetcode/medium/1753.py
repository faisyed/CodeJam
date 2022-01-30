class Solution:
    def maximumScore(self, a, b, c):
        x,y,z = sorted([a,b,c])
        res = 0
        while x>0 and y>0 and x+y>z:
            x-=1
            y-=1
            res+=1
        return res+(x+y)