class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        mx = max(candies)
        res = list()
        for val in candies:
            if val+extraCandies>=mx:
                res.append(True)
            else:
                res.append(False)
        return res