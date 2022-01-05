class Solution:
    def replaceDigits(self, s):
        lets = "abcdefghijklmnopqrstuvwxyz"
        mp = {}
        for i in range(26):
            mp[lets[i]] = i
        res = ""

        for i in range(0, len(s), 2):
            res += s[i]
            if i + 1 < len(s):
                ind = (mp[s[i]] + int(s[i + 1])) % 26
                res += lets[ind]
        return res