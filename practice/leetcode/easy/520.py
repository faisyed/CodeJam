class Solution:
    def detectCapitalUse(self, word):
        isLow = True
        isUp = True
        isCap = True
        for ch in word:
            if not ch.isupper():
                isUp = False
                break
        if isUp:
            return True
        for ch in word:
            if not ch.islower():
                isLow = False
                break
        if isLow:
            return True
        if not word[0].isupper():
            isCap = False
        if isCap:
            for i in range(1,len(word)):
                if word[i].isupper():
                    isCap = False
                    break
        if isCap:
            return True
        return False