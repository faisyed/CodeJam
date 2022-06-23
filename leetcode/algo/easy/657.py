class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mp = {'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}
        pos = [0,0]
        for ch in moves:
            nx = mp[ch]
            pos[0]+=nx[0]
            pos[1]+=nx[1]
        return pos[0]==0 and pos[1]==0