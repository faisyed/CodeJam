class Solution:
    def reformat(self, s: str) -> str:
        ch = ""
        dig = ""
        for c in s:
            if c.isdigit():
                dig+=c
            else:
                ch+=c
        dl = len(dig)
        cl = len(ch)
        if abs(dl-cl)>1:
            return ""
        res = ""
        if dl>=cl:
            i,j = 0,0
            while j<cl:
                res+=dig[i]+ch[j]
                i+=1
                j+=1
            res+=dig[i] if dl>cl else ""
        else:
            i,j = 0,0
            while i<dl:
                res+=ch[j]+dig[i]
                i+=1
                j+=1
            res+=ch[i]
        return res