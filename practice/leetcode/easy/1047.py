class Solution:
    def removeDuplicates(self, s):
        stack = []
        for ch in s:
            top = stack[-1] if stack else "0"
            if top == ch:
                stack.pop()
            else:
                stack.append(ch)
        res = ""
        for i in range(len(stack)):
            res += stack[i]
        return res
