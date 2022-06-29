class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = "13579"
        pos = -1
        for i in range(len(num)-1,-1,-1):
            if num[i] in odd:
                pos = i
                break
        return num[:pos+1]