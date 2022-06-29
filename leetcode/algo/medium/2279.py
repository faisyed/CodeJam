class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        tp = []
        for a,b in zip(rocks,capacity):
            tp.append([a,b])
        tp = sorted(tp,key=lambda x:x[1]-x[0])
        cnt = 0
        for v in tp:
            if v[1]-v[0]==0:
                cnt+=1
            elif v[1]-v[0]<=additionalRocks:
                cnt+=1
                additionalRocks -=v[1]-v[0]
        return cnt
                