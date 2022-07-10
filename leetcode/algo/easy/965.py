class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        return len(set(res))==1