class Solution:
    def checkAlmostEquivalent(self, word1, word2):
        mp1 = [0]*26
        mp2 = [0]*26
        for i in range(len(word1)):
            mp1[ord(word1[i]) - ord('a')]+=1
        for i in range(len(word2)):
            mp2[ord(word2[i]) - ord('a')]+=1
        for i in range(26):
            if abs(mp1[i]-mp2[i])>3:
                return False
        return True