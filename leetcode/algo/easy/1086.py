import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mp = {}
        for item in items:
            if item[0] not in mp:
                mp[item[0]] = [item[1]]
            else:
                mp[item[0]].append(item[1])
        res = []
        for k,v in mp.items():
            res.append([k,sum(heapq.nlargest(5,v))//5])
        res = sorted(res, key=lambda x:x[0])
        return res
                      