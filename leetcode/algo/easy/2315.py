class Solution:
    def countAsterisks(self, s: str) -> int:
        enc = False
        cnt = 0
        for ch in s:
            if ch == "*" and not enc:
                cnt+=1
            if ch == "|":
                enc = not enc
        return cnt