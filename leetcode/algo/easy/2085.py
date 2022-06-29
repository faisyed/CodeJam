from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        mp1 = Counter(words1)
        mp2 = Counter(words2)
        cnt = 0
        for k,v in mp1.items():
            if v == mp2[k] == 1:
                cnt+=1
        return cnt