class Solution:
    def wordPattern(self, pattern, s):
        mp1 = {}
        mp2 = {}
        ls = s.split(" ")
        if len(pattern) != len(ls):
            return False
        for ch, word in zip(pattern, ls):
            if ch not in mp1:
                if word in mp2:
                    return False
                else:
                    mp1[ch] = word
                    mp2[word] = ch
            else:
                if mp1[ch] != word:
                    return False
        return True