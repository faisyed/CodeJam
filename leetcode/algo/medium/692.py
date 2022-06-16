from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = Counter(words)
        mp = dict(sorted(mp.items(), key=lambda x:x[0]))
        mp = dict(sorted(mp.items(), key=lambda x:x[1], reverse=True))
        return list(mp.keys())[:k]