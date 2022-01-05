class Solution:
    def truncateSentence(self, s, k):
        sp = 0
        res = ""
        for ch in s:
            if ch == " ":
                sp += 1
                if sp == k:
                    break
                else:
                    res += ch
            else:
                res += ch
        return res

"""
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ls = s.split(" ")
        return " ".join(ls[:k])
"""