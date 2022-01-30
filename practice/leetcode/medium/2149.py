class Solution:
    def rearrangeArray(self, nums):
        pq = []
        nq = []
        for val in nums:
            if val<0:
                nq.append(val)
            else:
                pq.append(val)
        i= 0
        res = []
        while i<len(pq):
            res.append(pq[i])
            res.append(nq[i])
            i+=1
        return res