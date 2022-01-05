class Solution:
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        else:
            ind = word.index(ch)
            rev = word[:ind + 1]
            rev = rev[::-1]
            return rev + word[ind + 1:]
