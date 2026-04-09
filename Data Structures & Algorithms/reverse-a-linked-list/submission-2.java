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
        // Use an iterative approaach
        ListNode prevNode = null;
        ListNode currNode = head;

        while (currNode != null) {
            // temporarily store next so we don't lose it when flipping pointer
            ListNode nextTemp = currNode.next;
            // Flip the pointer here
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextTemp;
        }

        return prevNode;
    }
}
