from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones):
        stones = [(-1 * stone) for stone in stones]
        heapify(stones)
        while len(stones) >1:
            y = heappop(stones)
            x = heappop(stones)
            if x != y:
                heappush(stones, (y-x))
        return -1 * heappop(stones) if stones else 0