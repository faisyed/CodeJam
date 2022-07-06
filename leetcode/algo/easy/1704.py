class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = "aeiouAEIOU"
        l = len(s)
        i,j = 0, l//2
        c1,c2 = 0,0
        while j<l:
            if s[i] in vow:
                c1+=1
            if s[j] in vow:
                c2+=1
            i+=1
            j+=1
        return c1==c2