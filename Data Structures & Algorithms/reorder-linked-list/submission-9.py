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
        # Idea: Find the middle, reverse the second half, and merge the two halves
        # Time: O(n) and Space: O(1) if done iteratively

        # Find the middle using two pointers
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half iteratively
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev now contains the reversed second half
        # Merge the two halves iteratively
        head_ptr = head
        while prev:
            temp = head_ptr.next
            second_temp = prev.next
            head_ptr.next = prev
            prev.next = temp
            head_ptr = temp
            prev = second_temp

        