class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        if n%2==0:
            return [-1*i for i in range(n//2,0,-1)]+[i for i in range(1,n//2+1)]
        else:
            return [-1*i for i in range(n//2,0,-1)]+[0]+[i for i in range(1,n//2+1)]