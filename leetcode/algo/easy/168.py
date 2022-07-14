import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        up = string.ascii_uppercase
        mp = {i:ch for i,ch in enumerate(up)}
        res = ""
        while columnNumber!=0:
            x = (columnNumber-1)%26
            res+=mp[x]
            columnNumber = (columnNumber-1)//26
        return res[::-1]