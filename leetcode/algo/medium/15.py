class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for k in range(len(nums)-2):
            i,j = k+1,len(nums)-1
            while i<j and i>k and j>k:
                sm = nums[i]+nums[j]+nums[k]
                if sm == 0:
                    ls = tuple([nums[k],nums[i],nums[j]])
                    res.add(ls)
                    i+=1
                    j-=1
                elif sm>0:
                    j-=1
                elif sm<0:
                    i+=1
        return list(res)