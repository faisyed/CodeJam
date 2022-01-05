class Solution:
    def toLowerCase(self, s):
        res = ""
        for ch in s:
            if 65<=ord(ch)<=90:
                res+=chr(ord(ch)+32)
            else:
                res+=ch
        return res