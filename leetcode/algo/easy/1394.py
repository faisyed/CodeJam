class Solution:
    def findLucky(self, arr: List[int]) -> int:
        tp = [0]*501
        for v in arr:
            tp[v]+=1
        for i in range(500,-1,-1):
            if tp[i]==i and i!=0:
                return i
        return -1