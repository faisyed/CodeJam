import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {}
        lw = string.ascii_lowercase
        i,j = 0,0
        while j<26:
            if key[i] == ' ':
                i+=1
            else:
                if key[i] not in mp:
                    mp[key[i]] = lw[j]
                    i+=1
                    j+=1
                else:
                    i+=1
        res = ""
        for ch in message:
            if ch == " ":
                res+=ch
            else:
                res+=mp[ch]
        return res