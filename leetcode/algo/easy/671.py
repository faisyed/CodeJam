# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, res):
        if root:
            self.inorder(root.left,res)
            res.add(root.val)
            self.inorder(root.right,res)
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = set()
        self.inorder(root, res)
        res = sorted(res)
        return res[1] if len(res)>1 else -1