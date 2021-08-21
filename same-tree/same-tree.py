# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def recursiveSolution(node1, node2):
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            
            if not node1 and not node2:
                return True
            
            if node1.val != node2.val:
                return False
            
            
            return recursiveSolution(node1.left, node2.left) and recursiveSolution(node1.right, node2.right)
            
        
        
        return recursiveSolution(p, q)