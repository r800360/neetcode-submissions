# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        pointer = result

        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next

        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2

        return result.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            write = 0

            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    lists[write] = self.mergeTwoLists(lists[i], lists[i + 1])
                else:
                    lists[write] = lists[i]

                write += 1

            del lists[write:]

        return lists[0]