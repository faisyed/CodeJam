class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for cust in accounts:
            bal = sum(cust)
            if mx<bal:
                mx = bal
        return mx