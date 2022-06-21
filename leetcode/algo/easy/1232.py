class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        p1 = coordinates[0]
        p2 = coordinates[1]
        for i in range(2,len(coordinates)):
            p = coordinates[i]
            if (p[1]-p1[1])*(p2[0]-p1[0]) != (p2[1]-p1[1])*(p[0]-p1[0]):
                return False
        return True