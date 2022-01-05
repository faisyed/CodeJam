class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.upper()
        rev = s[::-1]
        res = ""
        cur_len = 0
        for ch in rev:
            if ch != "-":
                if cur_len<k:
                    res += ch
                    cur_len += 1
                else:
                    cur_len = 1
                    res += "-"+ch
        return res[::-1]