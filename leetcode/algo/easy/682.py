class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for op in ops:
            if op.isdigit() or op.startswith("-"):
                res.append(int(op))
            elif op == "+":
                res.append(res[-1]+res[-2])
            elif op == "D":
                res.append(2*res[-1])
            elif op == "C":
                res.pop()
        return sum(res)