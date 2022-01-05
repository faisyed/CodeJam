from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr):
        mp = Counter(arr)
        st = set()
        for key, val in mp.items():
            if val in st:
                return False
            st.add(val)
        return True