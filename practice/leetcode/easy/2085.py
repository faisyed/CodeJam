from collections import Counter
class Solution:
    def countWords(self, words1, words2):
        mp1 = Counter(words1)
        mp2 = Counter(words2)
        cnt = 0
        for key, val in mp1.items():
            if key in mp2:
                if val == 1 and mp2[key]==1:
                    cnt+=1
        return cnt