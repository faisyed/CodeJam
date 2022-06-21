class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = [True]*len(candies)
        for ind, c in enumerate(candies):
            if c+extraCandies<mx:
                res[ind]=False
        return res