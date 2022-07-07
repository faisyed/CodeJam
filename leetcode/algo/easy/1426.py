from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        mp = Counter(arr)
        cnt = 0
        for k,v in mp.items():
            if k+1 in mp:
                cnt+=v
        return cnt