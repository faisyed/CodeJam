class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        p = 0
        prev = 0
        csum = 0
        for i in range(k):
            csum+=calories[i]
        if csum>upper:
            p+=1
        elif csum<lower:
            p-=1
        for i in range(k, len(calories)):
            csum -= calories[prev]
            prev+=1
            csum += calories[i]
            if csum>upper:
                p+=1
            elif csum<lower:
                p-=1
        return p