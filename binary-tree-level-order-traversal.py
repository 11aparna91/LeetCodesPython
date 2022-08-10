# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## BFS
## Space Complexity= O(n) Time Complexity=O(n)  
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            queLen=len(q)
            level=[]
            for i in range(queLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        return res
