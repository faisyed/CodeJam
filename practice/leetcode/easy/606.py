class Solution:
    def tree2str(self, root):
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)+""
        if root.right is None:
            return str(root.val)+"("+self.tree2str(root.left)+")"
        return str(root.val)+"("+self.tree2str(root.left)+")"+"("+self.tree2str(root.right)+")"