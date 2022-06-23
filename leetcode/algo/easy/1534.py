class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1, len(arr)):
                    e1 = abs(arr[i]-arr[j])<=a
                    e2 = abs(arr[j]-arr[k])<=b
                    e3 = abs(arr[i]-arr[k])<=c
                    if e1 and e2 and e3:
                        cnt+=1
        return cnt