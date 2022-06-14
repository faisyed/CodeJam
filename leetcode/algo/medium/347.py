from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        st = dict(sorted(mp.items(), key= lambda mp:mp[1], reverse=True))
        res = []
        i = 0
        for ke,v in st.items():
            if i==k:
                break
            res.append(ke)
            i+=1
        return res