import string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ls = list(s)
        let = string.ascii_letters
        i,j = 0,len(ls)-1
        while i<j:
            if ls[i] in let and ls[j] in let:
                ls[i],ls[j] = ls[j],ls[i]
                i+=1
                j-=1
            if ls[i] not in let:
                i+=1
            if ls[j] not in let:
                j-=1
        return "".join(ls)
            