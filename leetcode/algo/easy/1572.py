class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sm = 0
        r = len(mat)
        c = len(mat[0])
        for i in range(r):
            for j in range(c):
                if i==j or i+j == c-1:
                    sm+=mat[i][j]
        return sm