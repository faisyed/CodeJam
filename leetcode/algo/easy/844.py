class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        st2 = []
        for ch in s:
            if st1 and ch=="#":
                st1.pop()
            elif ch.isalpha():
                st1.append(ch)
        for ch in t:
            if st2 and ch=="#":
                st2.pop()
            elif ch.isalpha():
                st2.append(ch)
        return "".join(st1) == "".join(st2)
        