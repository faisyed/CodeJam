class Solution:
    def maximum69Number (self, num: int):
        num = str(num)
        res = ""
        for ind,ch in enumerate(num):
            if ch == "6":
                res+="9"
                res+=num[ind+1:]
                break
            res+=ch
        return res