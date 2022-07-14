from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mp = Counter(s)
        prev = False
        for _,v in mp.items():
            if v%2!=0:
                if not prev:
                    prev = True
                else:
                    return False
        return True