class Solution:
    def isline(self, x1, y1, x2, y2, x, y):
        return (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1)

    def checkStraightLine(self, coordinates):
        cord1 = coordinates[0]
        cord2 = coordinates[1]
        y1 = cord1[1]
        x1 = cord1[0]
        x2 = cord2[0]
        y2 = cord2[1]
        for ind in range(2, len(coordinates)):
            x = coordinates[ind][0]
            y = coordinates[ind][1]
            if not self.isline(x1, y1, x2, y2, x, y):
                return False
        return True