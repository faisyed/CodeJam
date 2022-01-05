class Solution:
    def isPalindrome(self, s):
        rev = s[::-1]
        return rev == s

    def firstPalindrome(self, words):
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""