class Solution:
    def reverseVowels(self, s):
        vow = "aeiouAEIOU"
        i,j = 0,len(s)-1
        ls = list(s)
        while i<j:
            if ls[i] in vow and ls[j] in vow:
                ls[i],ls[j] = ls[j],ls[i]
                i+=1
                j-=1
            if ls[i] not in vow:
                i+=1
            if ls[j] not in vow:
                j-=1
        return "".join(ls)