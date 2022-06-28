# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            nonlocal diameter
            if not root:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            diameter=max(diameter , lheight + rheight)
            return max(lheight,rheight)+1  
            
        diameter=0
        height(root)
        return diameter
        
