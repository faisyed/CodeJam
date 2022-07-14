class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = len(piles)
        res = 0
        for i in range(l//3,l,2):
            res+=piles[i]
        return res