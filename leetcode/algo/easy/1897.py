class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp = {}
        for word in words:
            for ch in word:
                if ch in mp:
                    mp[ch]+=1
                else:
                    mp[ch]=1
        l = len(words)
        for _,v in mp.items():
            if v%l!=0:
                return False
        return True