from collections import Counter


class Solution:
    def minSetSize(self, arr):
        l = len(arr)
        mp = Counter(arr).most_common()
        sm = 0
        cnt = 0
        for key, freq in mp:
            sm += freq
            cnt += 1
            if l - sm <= l // 2:
                return cnt
