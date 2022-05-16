class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, h = 0, len(arr)
        while l<=h:
            mid = (l+h)//2
            if arr[mid]>arr[mid-1] and arr[mid+1]<arr[mid]:
                return mid
            elif arr[mid]<arr[mid+1]:
                l = mid+1
            else:
                h = mid-1
        return -1