class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        res = []
        for word in ls:
            res.append(word[::-1])
        return " ".join(res)