class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        mn = len(wordsDict)
        w1,w2 = -1, -1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
                if w2!=-1:
                    mn = min(mn, w1-w2)
            if wordsDict[i] == word2:
                w2 = i
                if w1!=-1 and w1!=w2:
                    mn = min(mn, w2-w1)
        return mn