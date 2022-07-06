class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = float("-inf")
        cur = 0
        for v in gain:
            cur += v
            mx = max(cur,mx)
        return max(mx, 0)