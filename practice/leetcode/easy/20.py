class Solution:
    def isValid(self, s):
        stack = []
        mp = {")":"(", "}":"{", "]":"["}
        for ch in s:
            if ch in mp:
                top = stack.pop() if stack else "0"
                if mp[ch] != top:
                    return False
            else:
                stack.append(ch)
        if len(stack)>0:
            return False
        return True