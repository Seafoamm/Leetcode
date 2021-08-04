# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        
        nodeList = []
        node = head
        while node:
            nodeList.append(node)
            node = node.next
        
        if len(nodeList) == 2:
            return ListNode(head.val, None) if n == 1 else head.next
        else:
            if not (-n + len(nodeList)):
                head = head.next
            else:
                nodeList[-n - 1].next = nodeList[-n + 1] if -n != -1 else None
            
        return head