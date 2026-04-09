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
        //Three approaches - Stack, recursively, and iteratively
        //Iteratively is best
        if (head == null) {
            return null;
        }
        // Approach 1: Stack
        Stack<ListNode> myStack = new Stack<ListNode>();
        ListNode current = head;

        while (current != null) {
            myStack.push(current);
            current = current.next;
        }

        ListNode newHead = myStack.pop();
        current = newHead;

        while (myStack.empty() == false) {
            ListNode nextNode = myStack.pop();
            current.next = nextNode;
            current = nextNode;
        }

        current.next = null;

        return newHead;
    }
}
