class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        sm = 0
        cnt = 0
        for tp in res:
            if cnt+tp[0]<=truckSize:
                sm+=tp[1]*tp[0]
                cnt+=tp[0]
            else:
                sm+=tp[1]*(truckSize-cnt)
                break
        return sm