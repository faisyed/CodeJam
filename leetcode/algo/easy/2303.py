class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev = 0
        cur = 0
        for up,t in brackets:
            tax+=(min(income,up)-prev)*t*0.01
            cur+=min(income,up)-prev
            prev = up
            if cur==income:
                break
        return tax
            