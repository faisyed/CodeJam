class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        mx = arr[l-1]
        res = [-1]*l
        for i in range(l-2,-1,-1):
            if arr[i]<=mx:
                res[i] = mx
            else:
                res[i] = mx
                mx = arr[i]
        return res