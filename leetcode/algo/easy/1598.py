class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []
        for log in logs:
            if st and log == "../":
                st.pop()
            elif log == "./":
                continue
            elif log!="../":
                st.append(log)
        return len(st)