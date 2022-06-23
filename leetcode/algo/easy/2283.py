from collections import Counter
class Solution:
    def condition1(self, num):
        l = len(num)
        tp = int(num)
        while tp!=0:
            x = tp%10
            if x>=l:
                return False
            tp//=10
        return True
    
    def condition2(self, num):
        mp = Counter(num)
        for i in range(len(num)):
            if mp.get(str(i),0) != int(num[i]):
                return False
        return True
    
    def digitCount(self, num: str) -> bool:
        return self.condition1(num) and self.condition2(num)   