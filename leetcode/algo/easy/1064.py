class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        res = -1
        l,h = 0, len(arr)-1
        while l<=h:
            mid = (l+h)//2
            if arr[mid]==mid:
                res = mid
                h = mid-1
            elif arr[mid]>mid:
                h = mid-1
            else:
                l = mid+1
        return res