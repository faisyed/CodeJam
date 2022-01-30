class Solution:
    def kWeakestRows(self, mat, k: int):
        mp = list()
        for ind in range(len(mat)):
            mp.append((sum(mat[ind]),ind))
        srt = sorted(mp)[:k]
        res = []
        for sm,ind in srt:
            res.append(ind)
        return res