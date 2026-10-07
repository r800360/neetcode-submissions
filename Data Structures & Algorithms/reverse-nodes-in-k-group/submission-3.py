# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Proceed iteratively, using O(n) time and O(1) space
        if k == 1:
            return head
        
        head_count = 1
        head_ptr = head
        while head_ptr.next:
            head_ptr = head_ptr.next
            head_count += 1
        
        curr = head
        result = head
        prev_tail = None

        while head_count >= k:
            prev = None
            head_ptr = curr

            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
        
            # Connect previous group to this reversed group
            if prev_tail:
                prev_tail.next = prev
            else:
                result = prev

            head_ptr.next = curr
            prev_tail = head_ptr
            
            head_count -= k
        
        return result