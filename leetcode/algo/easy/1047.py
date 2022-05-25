class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        st.append(s[0])
        for i in range(1, len(s)):
            if len(st)>0 and s[i] == st[-1]:
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)