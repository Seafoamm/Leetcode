/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0)
        {
            return null;
        }
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(new ListNodeComparator());
        
        for (ListNode list : lists)
        {
            if (list != null)
            {
                pq.add(list);
            }
        }
        
        ListNode sentinel = new ListNode();
        ListNode head = sentinel;
        
        while (!pq.isEmpty())
        {
            ListNode nextNode = pq.poll();
            head.next = nextNode;
            if (nextNode.next != null)
            {
                pq.add(nextNode.next);    
            }
            head = head.next;
            
        }
        
        return sentinel.next;
    }
    
    class ListNodeComparator implements Comparator<ListNode>
    {
        public int compare(ListNode a, ListNode b)
        {
            return a.val - b.val;
        }
    }
}