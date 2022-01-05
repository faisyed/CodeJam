class Solution:
    def guessNumber(self, n):
        l = 1
        h = n
        while l<=h:
            mid = (l+h)//2
            res = guess(mid)
            if res==0:
                return mid
            elif res==-1:
                h = mid-1
            else:
                l = mid+1