# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is not None:
            return self.Symmetric(root.left, root.right)
        else:
            return True
    def Symmetric(self, left, right):
        if left is not None and right is not None:
            if left.val==right.val:
                return self.Symmetric(left.left, right.right) and self.Symmetric(left.right, right.left)
            else:
                return False
        
        if left is None and right is None:
            return True
        
        return False
        
