# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        currNode = head
        if not currNode:
            return None
        newHead = head.next if head.next else head
        prev = None
        while(currNode):
            first = currNode
            second = currNode.next
            if not second:
                break
            else:
                temp = second.next
                second.next = first
                first.next = temp
                if prev:
                    prev.next = second
                prev = first
                currNode = temp
                
        return newHead
        
        
        
    # loop until we reach the end of the linked list, so the original 2nd node in the pair.next == null (even case) or the 2nd pair IS null (odd case)
    # save the original next of 2nd node the in pair = temp
    # set 2nd node of pair.next = 1st node
    # set 1st node of pair.next = temp
    # next node = temp
    
    # missed linking it to the previous one
    