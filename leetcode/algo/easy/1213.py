from collections import Counter
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        c = Counter(arr1+arr2+arr3)
        res = []
        for k,v in c.items():
            if v==3:
                res.append(k)
        return res