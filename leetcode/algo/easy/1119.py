class Solution:
    def removeVowels(self, s: str) -> str:
        vow = "aeiou"
        res = ""
        for ch in s:
            if ch not in vow:
                res+=ch
        return res