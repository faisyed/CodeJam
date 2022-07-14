class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ls = text.split()
        res = []
        for i in range(len(ls)-2):
            w1,w2,w3 = ls[i],ls[i+1],ls[i+2]
            if w1==first and w2==second:
                res.append(w3)
        return res