class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        tp = str(num)
        cnt = 0
        for i in range(len(tp)-k+1):
            div = int(tp[i:i+k])
            if div!=0 and num%div==0:
                cnt+=1
        return cnt