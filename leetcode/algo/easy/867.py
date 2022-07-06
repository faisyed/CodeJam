class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        mat = [[0 for i in range(m)] for j in range(n)]
        for i, row in enumerate(matrix):
            for j,v in enumerate(row):
                mat[j][i] = v
        return mat