class Solution:
    def isLongPressedName(self, name, typed):
        p1 = 0
        p2 = 0
        m = len(name)
        n = len(typed)
        while p2<n:
            if p1<m and name[p1] == typed[p2]:
                p1 += 1
            elif p2 == 0 or typed[p2] != typed[p2-1]:
                return False
            p2 += 1
        return p1 == m