from collections import Counter
class Solution:
    def kthDistinct(self, arr, k):
        st = set(arr)
        l = len(st)
        if k>l:
            return ""
        mp = Counter(arr)
        res = {}
        i = 1
        for ch in arr:
            if mp[ch]==1:
                res[i]=ch
                i+=1
        return res.get(k,"")