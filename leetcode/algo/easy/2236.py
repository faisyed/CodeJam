class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        p = root.val
        l = root.left.val
        r = root.right.val
        return p == l+r