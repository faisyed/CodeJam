class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = {}
        for ch in arr:
            if ch in mp:
                mp[ch]+=1
            else:
                mp[ch]=1
        ls = []
        for key,v in mp.items():
            if v==1:
                ls.append(key)
        return ls[k-1] if k<=len(ls) else ""