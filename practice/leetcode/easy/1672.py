class Solution:
    def maximumWealth(self, accounts):
        mx = -10
        for customer in accounts:
            sm = sum(customer)
            if mx<sm:
                mx = sm
        return mx