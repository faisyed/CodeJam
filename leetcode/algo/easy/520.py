class Solution:
    def isLower(self, word):
        for ch in word:
            if not ch.islower():
                return False
        return True
    
    def isUpper(self, word):
        for ch in word:
            if not ch.isupper():
                return False
        return True
    
    def isTitle(self, word):
        if not word[0].isupper():
            return False
        for i in range(1,len(word)):
            if not word[i].islower():
                return False
        return True
    
    def detectCapitalUse(self, word: str) -> bool:
        return self.isLower(word) or self.isUpper(word) or self.isTitle(word)