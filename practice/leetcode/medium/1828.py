from math import sqrt


class Solution:
    def distance(self, point, center):
        return sqrt((center[0] - point[0]) ** 2 + (center[1] - point[1]) ** 2)

    def countPoints(self, points, queries):
        res = []
        for q in queries:
            center = q[:2]
            rad = q[2]
            cnt = 0
            for point in points:
                if self.distance(point, center) <= rad:
                    cnt += 1
            res.append(cnt)
        return res