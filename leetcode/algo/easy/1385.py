class Solution:
    def valid(self, v, arr2,d):
        l, h = 0, len(arr2)
        while l<h:
            mid = (l+h)//2
            if abs(v-arr2[mid])<=d:
                return False
            elif arr2[mid]>v:
                h = mid
            else:
                l = mid+1
        return True
    
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        return sum(self.valid(x, arr2,d) for x in arr1)