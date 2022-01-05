class Solution:
    def balancedStringSplit(self, s):
        bal = 0
        res = 0
        for ch in s:
            if ch == "L":
                bal+=1
            elif ch == "R":
                bal-=1
            if bal == 0:
                res+=1
        return res