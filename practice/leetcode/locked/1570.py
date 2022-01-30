class SparseVector:
    def __init__(self, nums):
        self.mat = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        res = 0
        for i in range(len(self.mat)):
            res += self.mat[i] * vec.mat[i]
        return res