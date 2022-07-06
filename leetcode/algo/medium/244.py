class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.mp = {}
        for i,w in enumerate(wordsDict):
            if w not in self.mp:
                self.mp[w] = [i]
            else:
                self.mp[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        ind1 = self.mp[word1]
        ind2 = self.mp[word2]
        mn = float('inf')
        for x in ind1:
            for y in ind2:
                mn = min(mn, abs(x-y))
        return mn
