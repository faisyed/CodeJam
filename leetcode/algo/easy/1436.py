class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src,dest = set(),set()
        for path in paths:
            src.add(path[0])
            dest.add(path[1])
        res = dest-src
        return res.pop()