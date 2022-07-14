class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sm, eq = 0,0
        for v in nums:
            if v<target:
                sm+=1
            elif v==target:
                eq+=1
        return list(range(sm,sm+eq))