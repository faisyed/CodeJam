class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        cur = 0
        cnt = 0
        for i in range(len(weight)):
            if cur+weight[i] > 5000:
                break
            cur+=weight[i]
            cnt+=1
        return cnt