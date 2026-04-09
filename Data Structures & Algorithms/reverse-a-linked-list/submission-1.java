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
    public ListNode reverseList(ListNode head) {
        // Use a recursive approach
        // Base Case
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return head;
        }

        //Go to the end and get the new head
        ListNode result = reverseList(head.next);

        //Flip the pointer along the way
        head.next.next = head;
        
        //Clean up - current node is new tail so next must be null
        head.next = null;

        //Return new head
        return result;
    }
}
