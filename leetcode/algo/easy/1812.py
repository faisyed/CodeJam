class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        mp = {}
        for i, ch in zip(range(1,9),"abcdefgh"):
            mp[ch]=i
        sm = mp[coordinates[0]]+int(coordinates[1])
        return False if sm%2==0 else True