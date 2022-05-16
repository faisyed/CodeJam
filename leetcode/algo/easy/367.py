class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,h = 0, num
        while l<=h:
            mid = (l+h)//2
            n = mid*mid
            if n == num:
                return True
            elif n>num:
                h = mid-1
            else:
                l = mid+1
        return False