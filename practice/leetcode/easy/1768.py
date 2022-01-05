class Solution:
    def mergeAlternately(self, word1, word2):
        i, j = 0, 0
        l1 = len(word1)
        l2 = len(word2)
        res = ""
        while i<l1 and j<l2:
            res+=word1[i]+word2[j]
            i+=1
            j+=1
        while i<l1:
            res+=word1[i]
            i+=1
        while j<l2:
            res+=word2[j]
            j+=1
        return res