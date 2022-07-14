class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        arr.sort()
        rm = 5*l//100
        sm = 0
        
        for i in range(rm, l-rm):
            sm+=arr[i]
        return sm/(l-2*rm)