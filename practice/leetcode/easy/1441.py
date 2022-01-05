class Solution:
    def buildArray(self, target, n):
        res = list()
        ind = 0
        val = 1
        while val<=n and ind<len(target):
            if val==target[ind]:
                res.append("Push")
                ind += 1
            else:
                res.append("Push")
                res.append("Pop")
            val += 1
        return res