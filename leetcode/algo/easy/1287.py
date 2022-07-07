class Solution:
    def getFirst(self, key, arr):
        l,r = 0,len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]<key:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(1,4):
            ind = (len(arr)*i)//4
            st = self.getFirst(arr[ind], arr)
            if arr[st] == arr[st+len(arr)//4]:
                return arr[st]