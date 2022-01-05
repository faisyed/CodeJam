class Solution:
    def getSum(self, num):
        sm = 0
        while num != 0:
            x = num % 10
            sm += x
            num //= 10
        return sm

    def countBalls(self, lowLimit, highLimit):
        mp = defaultdict(int)
        mx = 0
        for i in range(lowLimit, highLimit + 1):
            box = self.getSum(i)
            mp[box] += 1
            if mp[box] > mx:
                mx = mp[box]
        return mx