# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [2,4,6,8] -> [2,8,4,6]
        # [2,4,6,8,10] -> [2,10,4,8,6]
        # [1,2,3,4] -> [1,4,2,3]
        # [1,2,3,4,5] -> [1,5,2,4,3]
        # [0, 1, ..., n-1] -> [0, n-1, 1, n-2, 2, n-3, ...]
        # Time: O(n^2) and Space: O(n)
        # Time: n + (n - 2) + (n - 4) + ... + 1 = O(n^2)
        # Space: Dummy ListNode on every recursive call, recursive call stack reaches about n/2 levels -> O(n) stack space
        if not head:
            return None
        if not head.next:
            return
        if not head.next.next:
            return
        
        prevNode = ListNode(next=head)
        currNode = head

        while currNode.next:
            prevNode = prevNode.next
            currNode = currNode.next

        currNode.next = head.next
        head.next = prevNode.next
        prevNode.next = None

        self.reorderList(head.next.next)