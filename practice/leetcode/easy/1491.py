class Solution:
    def average(self, salary:):
        mn = float("inf")
        mx = float("-inf")
        sm = 0
        n = 0
        for val in salary:
            n += 1
            sm += val
            if val>mx:
                mx = val
            if val<mn:
                mn = val
        sm = sm - mx - mn
        return round(sm / (n-2), 5)