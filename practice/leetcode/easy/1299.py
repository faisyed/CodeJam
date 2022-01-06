class Solution:
    def replaceElements(self, arr):
        res = [-1]
        mx = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > mx:
                res.append(mx)
                mx = arr[i]
            else:
                res.append(mx)
        return res[::-1]