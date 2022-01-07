class Solution:
    def heightChecker(self, heights):
        tp = heights.copy()
        tp.sort()
        cnt = 0
        for v1,v2 in zip(tp,heights):
            if v1!=v2:
                cnt+=1
        return cnt