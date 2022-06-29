class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sm = 0
        cost.sort(reverse=True)
        for i in range(len(cost)):
            if i%3!=2:
                sm+=cost[i]
        return sm