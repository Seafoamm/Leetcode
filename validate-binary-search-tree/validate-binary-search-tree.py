# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def validate(node, maxValue=float('inf'), minValue=float('-inf')):
            if not node:
                return True
            # print(f'{node.val, maxValue, minValue}')
            if node.val >= maxValue or node.val <= minValue:
                # print('value is outside bounds')
                return False
            else:
                return validate(node.left, min(maxValue, node.val), minValue) and validate(node.right, maxValue, max(minValue, node.val))
        
        return validate(root)