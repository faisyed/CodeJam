class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 0, n
        while l<h:
            mid = (l+h)//2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                h = mid
        return l