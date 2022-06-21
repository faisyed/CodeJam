from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        prev = 0
        res = []
        for ind,ch in enumerate(paragraph):
            if ch.isspace() or not ch.isalpha():
                res.append(paragraph[prev:ind])
                prev = ind+1
        res.append(paragraph[prev:])
        res = [v for v in res if len(v)>0]
        mp = Counter(res)
        mp = dict(sorted(mp.items(),key=lambda x:x[1], reverse=True))
        for k,v in mp.items():
            if k not in banned:
                return k