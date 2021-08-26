# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        if not k:
            return head
        
        curr = head
        length = 1
        
        while curr.next:
            curr = curr.next
            length += 1
            
        k %= length
        if not k:
            return head
        root = head
        
        while length - k - 1 > 0:
            root = root.next
            length -= 1
        sentinel = root.next
        root.next = None
        
        curr.next = head
        
        return sentinel