from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        ls = Counter(words).most_common()
        ls.sort(key=lambda x:x[0])
        ls.sort(key=lambda x:x[1], reverse=True)
        ind = 0
        res = list()
        for key, freq in ls:
            if ind == k:
                break
            res.append(key)
            ind += 1
        return res