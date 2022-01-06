class Solution:
    def judgeCircle(self, moves):
        mp = {"U": (-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}
        st = (0,0)
        for ch in moves:
            st = (st[0]+mp[ch][0], st[1]+mp[ch][1])
        return st == (0,0)