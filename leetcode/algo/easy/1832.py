class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ar = [0]*26
        for ch in sentence:
            ar[ord(ch)-ord('a')]+=1
        for v in ar:
            if v==0:
                return False
        return True