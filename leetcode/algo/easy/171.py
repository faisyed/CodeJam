import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        up = string.ascii_uppercase
        mp = {ch:i+1 for i,ch in enumerate(up)}
        res = 0
        for ch in columnTitle:
            res = res*26
            res+=mp[ch]
        return res