class Solution:
    def isSameAfterReversals(self, num):
        if num==0:
            return True
        x = num%10
        return not x==0