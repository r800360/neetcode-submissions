"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        
        head_ptr = head
        copy_head = Node(x = head.val)
        copy_ptr = copy_head
        copy_htable = {}
        copy_htable[head_ptr] = copy_ptr
        while head_ptr.next:
            copy_ptr.next = Node(head_ptr.next.val)
            head_ptr = head_ptr.next
            copy_ptr = copy_ptr.next
            copy_htable[head_ptr] = copy_ptr

        
        head_ptr = head
        copy_ptr = copy_head
        
        while head_ptr.next:
            if not head_ptr.random:
                copy_ptr.random = None
            else:
                copy_ptr.random = copy_htable[head_ptr.random]
            head_ptr = head_ptr.next
            copy_ptr = copy_ptr.next
        if not head_ptr.random:
                copy_ptr.random = None
        else:
            copy_ptr.random = copy_htable[head_ptr.random]
        return copy_head