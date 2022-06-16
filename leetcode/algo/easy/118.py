class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows==1:
            return res
        for i in range(1,numRows):
            tp = res[i-1]
            ntp = [tp[0]]
            for j in range(1,len(tp)):
                ntp.append(tp[j-1]+tp[j])
            ntp.append(tp[len(tp)-1])
            res.append(ntp)
        return res