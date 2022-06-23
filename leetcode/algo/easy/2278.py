class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l,c = 0,0
        for ch in s:
            l+=1
            if ch==letter:
                c+=1
        return (c*100//l)