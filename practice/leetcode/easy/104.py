class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            lheight = self.maxDepth(root.left)
            rheight = self.maxDepth(root.right)
            return max(lheight, rheight) + 1
