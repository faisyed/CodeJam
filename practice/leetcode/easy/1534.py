class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        cnt = 0
        l = len(arr)
        for i in range(l-2):
            for j in range(i+1, l-1):
                if abs(arr[i] - arr[j])<=a:
                    for k in range(j+1, l):
                        eq1 = abs(arr[j]-arr[k])<=b
                        eq2 = abs(arr[k]-arr[i])<=c
                        if all((eq1,eq2)):
                            cnt+=1
        return cnt