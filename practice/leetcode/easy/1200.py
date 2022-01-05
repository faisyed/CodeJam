class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        mn = float("inf")
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            mn = min(mn, diff)
        res = list()
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff == mn:
                res.append([arr[i], arr[i+1]])
        return res