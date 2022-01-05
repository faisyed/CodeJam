class Solution:
    def countPoints(self, rings):
        mp = {}
        for i in range(0, len(rings), 2):
            if rings[i+1] not in mp:
                mp[rings[i+1]] = set((rings[i],))
            else:
                mp[rings[i+1]].add(rings[i])
        cnt = 0
        for rod, col in mp.items():
            if len(col)==3:
                cnt+=1
        return cnt