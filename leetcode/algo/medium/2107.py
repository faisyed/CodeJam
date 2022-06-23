from collections import Counter
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        mp = Counter(candies[k:])
        res = len(mp)
        for i in range(k,len(candies)):
            mp[candies[i]]-=1
            if mp[candies[i]] == 0:
                del mp[candies[i]]
            mp[candies[i-k]]+=1
            res = max(res,len(mp))
        return res