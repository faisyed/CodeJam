class Solution:
    def isOdd(self, n):
        return n % 2 != 0

    def threeConsecutiveOdds(self, arr):
        for i in range(0, len(arr) - 2):
            if self.isOdd(arr[i]) and self.isOdd(arr[i + 1]) and self.isOdd(arr[i + 2]):
                return True
        return False