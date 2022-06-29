class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = float('inf')
        for i in range(1,len(arr)):
            mn = min(mn,abs(arr[i]-arr[i-1]))
        res = []
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] == mn:
                res.append([arr[i-1],arr[i]])
        return res