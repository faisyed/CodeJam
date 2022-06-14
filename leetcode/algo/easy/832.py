class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for row in image:
            tp = row[::-1]
            for i in range(len(tp)):
                tp[i] = 0 if tp[i]==1 else 1
            res.append(tp)
        return res