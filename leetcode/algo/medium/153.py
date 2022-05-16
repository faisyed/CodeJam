class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l, h = 0, len(nums)-1
        if nums[h]>nums[0]:
            return nums[0]
        while l<h:
            mid = (l+h)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[0]<nums[mid]:
                l = mid+1
            else:
                h = mid-1
        return -1