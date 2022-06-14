from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        st = Counter(stones)
        cnt = 0
        for j in jewels:
            cnt+=st[j]
        return cnt