# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        def construct(left = 0, right = len(nums) - 1):
            if left > right:
                return None
            mid = left + (right - left) // 2
            current = TreeNode(nums[mid])
            current.left = construct(left, mid - 1)
            current.right = construct(mid + 1, right)
            
            return current
        
        return construct()
        
        