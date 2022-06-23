class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        pos = 1
        k = 1
        for i in range(1,len(nums)):
            if nums[i]!=prev:
                prev = nums[i]
                nums[i],nums[pos] = nums[pos],nums[i]
                pos+=1
                k+=1
        return k