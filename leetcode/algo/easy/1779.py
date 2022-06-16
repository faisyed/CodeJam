class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = 9999999
        res = -1
        for ind, p in enumerate(points):
            if p[0]!=x and p[1]!=y:
                continue
            curdist = abs(p[0]-x)+abs(p[1]-y)
            if curdist<dist:
                dist = curdist
                res = ind
        return res