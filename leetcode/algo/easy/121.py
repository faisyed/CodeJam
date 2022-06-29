class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = 0
        mn = float('inf')
        for i in range(len(prices)):
            if mn>prices[i]:
                mn = prices[i]
            elif prices[i]-mn>pr:
                pr = prices[i]-mn
        return pr
            