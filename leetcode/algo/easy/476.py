class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        res = ""
        for ch in b:
            res+= "0" if ch == "1" else "1"
        return int(res,2)