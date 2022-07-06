class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = 0
        for i, v in enumerate(word):
            if v == ch:
                pos = i
                break
        rev = word[:pos+1]
        return rev[::-1]+word[pos+1:]