class Solution:
    def countOdds(self, low, high):
        cnt = 0
        if low%2!=0 or high%2!=0:
            cnt+=1
        cnt+=(high-low)//2
        return cnt