class Solution:
    def removeVowels(self, s):
        vow = "aeiou"
        res = ""
        for ch in s:
            if ch not in vow:
                res+=ch
        return res