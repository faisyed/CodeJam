class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = "aeiouAEIOU"
        av = ""
        for ch in s:
            if ch in vow:
                av+=ch
        res = ""
        i = len(av)-1
        for ch in s:
            if ch in vow:
                res+=av[i]
                i-=1
            else:
                res+=ch
        return res