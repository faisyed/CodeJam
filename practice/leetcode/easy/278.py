class Solution:
    def firstBadVersion(self, n):
        l = 1
        h = n
        while l<h:
            mid = (l+h)//2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid+1
        return l