# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbersHelper(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        # if not l1.next and not l2.next:
            # if l1.val + l2.val + carry != 0:
            #     l1.next = ListNode()
            #     l2.next = ListNode()
            # else:
            #     return None
        res = l1.val + l2.val + carry
        sumVal = res % 10
        carryVal = res // 10
        l1.val = sumVal
        if not l1.next and not l2.next and carryVal == 0:
            return l1
        if not l1.next:
            l1.next = ListNode()
        if not l2.next:
            l2.next = ListNode()
        l1.next = self.addTwoNumbersHelper(l1.next, l2.next, carryVal)
        return l1

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(m + n) time and O(1) space
        return self.addTwoNumbersHelper(l1, l2, 0)