from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = Counter(arr)
        st = set()
        for k,v in mp.items():
            if v in st:
                return False
            else:
                st.add(v)
        return True