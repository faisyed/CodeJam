class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        l1,l2 = len(word1),len(word2)
        res = ""
        while i<l1 or j<l2:
            c1 = word1[i] if i<l1 else ""
            c2 = word2[j] if j<l2 else ""
            i+=1
            j+=1
            res+=c1+c2
        return res