class Solution:
    def halvesAreAlike(self, s):
        l = len(s)
        mid = l//2
        vow = "aeiouAEIOU"
        c1,c2 = 0,0
        for i in range(mid):
            if s[i] in vow:
                c1+=1
            if s[mid+i] in vow:
                c2+=1
        return c1==c2