class Solution:
    def traverse(self, root, res):
        if root is None:
            return
        self.traverse(root.left,res)
        self.traverse(root.right,res)
        res.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(root, res)
        return res