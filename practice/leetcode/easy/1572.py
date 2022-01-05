class Solution:
    def diagonalSum(self, mat):
        sm1,sm2 = 0,0
        n = len(mat)
        for i in range(n):
            sm1 += mat[i][i]
            sm2 += mat[i][n-i-1]
        if n%2!=0:
            sm2 -= mat[n//2][n//2]
        return sm1+sm2