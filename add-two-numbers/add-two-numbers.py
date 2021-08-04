# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        carry = 0

        while l1:
            digit = l1.val + carry
            if l2:
                digit += l2.val
                l2 = l2.next
            else:
                if not carry:
                    break
            
            l1.val = digit % 10
            carry = digit // 10
            
            if not l1.next and l2:
                l1.next = l2
                l2 = None
                
            if not l1.next:
                if carry:
                    l1.next = ListNode(1)
                    carry = 0
                    
                    
            l1 = l1.next
                
        
        
        return head

            