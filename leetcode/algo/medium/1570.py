class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = {}
        for i,v in enumerate(nums):
            if v!=0:
                self.mp[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i,v in vec.mp.items():
            res+=self.mp.get(i,0)*v
        return res