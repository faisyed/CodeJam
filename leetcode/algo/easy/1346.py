class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mp = {}
        for v in arr:
            if 2*v in mp or v/2 in mp:
                return True
            mp[v]=1
        return False