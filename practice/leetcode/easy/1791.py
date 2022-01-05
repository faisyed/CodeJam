class Solution:
    def findCenter(self, edges):
        cnt = 0
        mp = {}
        for edge in edges:
            if edge[0] not in mp:
                mp[edge[0]] = 1
                cnt+=1
            else:
                mp[edge[0]] += 1
            if edge[1] not in mp:
                mp[edge[1]] = 1
                cnt+=1
            else:
                mp[edge[1]] += 1
        res = -1
        for key, val in mp.items():
            if val==cnt-1:
                res = key
                break
        return res

"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]
"""