class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for ch in s:
            v = ord(ch)
            if 65<=v<=90:
                res+=chr(ord('a')+(v-ord('A')))
            else:
                res+=ch
        return res