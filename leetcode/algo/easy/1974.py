class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = "a"
        cnt = 0
        for ch in word:
            diff = abs(ord(ch)-ord(prev))%26
            cnt+=min(diff,26-diff)
            cnt+=1
            prev=ch
        return cnt