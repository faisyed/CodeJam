class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        res = ""
        for i,ch in enumerate(s):
            if ch == '6':
                res+='9'+s[i+1:]
                break
            else:
                res+=ch
        return int(res)