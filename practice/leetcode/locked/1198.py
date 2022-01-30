from collections import Counter

class Solution:
    def smallestCommonElement(self, mat) -> int:
        ar = [0] * 10001
        n, m = len(mat), len(mat[0])
        for j in range(m):
            for i in range(n):
                ar[mat[i][j]] += 1
                if ar[mat[i][j]] == n:
                    return mat[i][j]
        return -1
