class Solution:
    def average(self, salary: List[int]) -> float:
        mn,mx = float('inf'),float('-inf')
        l = 0
        sm = 0
        for v in salary:
            l+=1
            sm+=v
            if mn>v:
                mn = v
            if mx<v:
                mx = v
        return (sm-mx-mn)/(l-2)