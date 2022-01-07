class Solution:
    def construct2DArray(self, original, m, n):
        if m*n != len(original):
            return []
        ind = 0
        res = list()
        for i in range(m):
            tp = []
            for j in range(n):
                tp.append(original[ind])
                ind += 1
            res.append(tp)
        return res