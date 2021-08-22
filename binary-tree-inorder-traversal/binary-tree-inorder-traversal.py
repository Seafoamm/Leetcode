# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
        """
        if not root:
            return []
        stack = []
        output = []
        current = root
        stack.append(current)
        if current:
            current = current.left
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            top = stack.pop()
            output.append(top.val)
            current = top.right

        
        return output