class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        if rowIndex==0:
            return res[0]
        for i in range(1,rowIndex+1):
            tp = res[i-1]
            ntp = [tp[0]]
            for j in range(1,len(tp)):
                ntp.append(tp[j]+tp[j-1])
            ntp.append(tp[len(tp)-1])
            res.append(ntp)
        return res[rowIndex]