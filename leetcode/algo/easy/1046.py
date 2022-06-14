import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i,v in enumerate(stones):
            stones[i]=-1*v
        heapq.heapify(stones)
        while len(stones)>1:
            y,x = heapq.heappop(stones),heapq.heappop(stones)
            heapq.heappush(stones,y-x)
        return -1*heapq.heappop(stones)