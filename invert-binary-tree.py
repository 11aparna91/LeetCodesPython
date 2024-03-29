# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left,root.right= self.invertTree(root.right),self.invertTree(root.left)
            return root
####################################### DFS #########
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                node.left,node.right= node.right,node.left
                stack.extend([node.left,node.right])
        return root
################## BFS ###################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que= collections.deque([root])
        while que:
            node=que.popleft()
            if node:
                node.left,node.right= node.right,node.left
                que.append(node.left)
                que.append(node.right)
        return root
