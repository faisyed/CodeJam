class Solution:
    def countDigits(self, num):
        cnt = 0
        while num!=0:
            x = num%10
            cnt+=1
            num//=10
        return cnt
    
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res+=1 if self.countDigits(num)%2==0 else 0
        return res