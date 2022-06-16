class Solution:
    def traverse(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(root, res)
        return res