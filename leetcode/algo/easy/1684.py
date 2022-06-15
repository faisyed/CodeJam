class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        fl = True
        for w in words:
            for ch in w:
                if ch not in allowed:
                    fl = False
                    break
            if fl:
                cnt+=1
            else:
                fl = True
        return cnt
            