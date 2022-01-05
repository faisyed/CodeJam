import string


class Solution:
    def reverseOnlyLetters(self, s):
        ls = list(s)
        i, j = 0, len(s) - 1
        small = string.ascii_lowercase
        cap = string.ascii_uppercase
        while i < j:
            if (ls[i] in small or ls[i] in cap) and (ls[j] in small or ls[j] in cap):
                ls[i], ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
            if not (ls[i] in small or ls[i] in cap):
                i += 1
            if not (ls[j] in small or ls[j] in cap):
                j -= 1
        return "".join(ls)
