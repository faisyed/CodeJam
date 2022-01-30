class Solution:
    def findSecondMinimumValue(self, root):
        st = set()
        def dfs(root):
            if root is not None:
                st.add(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        if len(st)==1:
            return -1
        fmn, smn = float('inf'),float('inf')
        for val in st:
            if val<fmn:
                smn = fmn
                fmn = val
            elif val<smn:
                smn = val
        return smn