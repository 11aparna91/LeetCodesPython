######## Problem Number 589 ############
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        stack=[]
        
        q=collections.deque([root])
        
        while q:
            node=q.popleft()
            stack.append(node.val)
            for c in reversed(node.children):
                q.appendleft(c)
        
        return stack
        
        
        
###################################

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return
        stack=[]
        
        q=collections.deque([root])
        
        while q:
            node=q.popleft()
            stack.append(node.val)
            for c in reversed(node.children):
                q.appendleft(c)
        
        return stack
        
   
        
        
        
        
        
        
        
        
        
        
        
            
        
        
