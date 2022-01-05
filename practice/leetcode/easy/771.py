class Solution:
    def numJewelsInStones(self, jewels, stones):
        st = set(jewels)
        cnt = 0
        for stone in stones:
            if stone in st:
                cnt+=1
        return cnt