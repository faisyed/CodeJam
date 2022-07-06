class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        mp = {}
        for i, w in enumerate(wordsDict):
            if w not in mp:
                mp[w] = [i]
            else:
                mp[w].append(i)
        r1 = mp[word1]
        r2 = mp[word2]
        mn = float("inf")
        for v in r1:
            for w in r2:
                mn = min(mn, abs(v-w))
        return mn