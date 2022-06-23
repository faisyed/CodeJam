class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = "aeiou"
        cnt = 0
        for i in range(k):
            if s[i] in vow:
                cnt+=1
        res = max(0,cnt)
        prev = 0
        for i in range(k,len(s)):
            if s[prev] in vow:
                cnt -= 1
            prev += 1
            if s[i] in vow:
                cnt +=1
            res = max(res,cnt)
        return res