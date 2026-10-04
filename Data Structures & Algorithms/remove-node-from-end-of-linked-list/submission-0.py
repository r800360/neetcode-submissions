# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        head_ptr = head
        num_nodes = 1

        while (head_ptr.next):
            num_nodes += 1
            head_ptr = head_ptr.next
        
        remove_idx = num_nodes-n

        if remove_idx == 0:
            if head.next:
                head = head.next
                return head
            else:
                return None

        current = head
        for i in range(remove_idx-1):
            current = current.next

        if current.next is None:
            return None

        current.next = current.next.next
        return head