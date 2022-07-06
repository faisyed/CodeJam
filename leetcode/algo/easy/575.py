class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        st = set(candyType)
        if n//2>=len(st):
            return len(st)
        return n//2