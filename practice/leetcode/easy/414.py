class Solution:
    def thirdMax(self, nums):
        mx = set()
        for num in nums:
            if num not in mx:
                mx.add(num)
            if len(mx)>3:
                mx.remove(min(mx))
        if len(mx) == 3:
            return min(mx)
        return max(mx)