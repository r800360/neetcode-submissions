class ListNode:
    def __init__(self, key=0, val=0, prev=None, nt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nt = nt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_map = {}
        self.head_node = ListNode()
        self.tail_node = ListNode()
        self.head_node.nt = self.tail_node
        self.tail_node.prev = self.head_node
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache_map:
            curr_key = self.cache_map[key].key
            curr_value = self.cache_map[key].val
            self.cache_map[key].prev.nt = self.cache_map[key].nt
            self.cache_map[key].nt.prev = self.cache_map[key].prev
            del self.cache_map[curr_key]
            self.cache_map[key] = ListNode(key=key, val=curr_value, prev=self.head_node, nt=self.head_node.nt)
            self.head_node.nt.prev = self.cache_map[key]
            self.head_node.nt = self.cache_map[key]
            return curr_value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            curr_key = self.cache_map[key].key
            self.cache_map[key].prev.nt = self.cache_map[key].nt
            self.cache_map[key].nt.prev = self.cache_map[key].prev
            del self.cache_map[curr_key]
            self.cache_map[key] = ListNode(key=key, val=value, prev=self.head_node, nt=self.head_node.nt)
            self.head_node.nt.prev = self.cache_map[key]
            self.head_node.nt = self.cache_map[key]
        else:
            self.cache_map[key] = ListNode(key=key, val=value, prev=self.head_node, nt=self.head_node.nt)
            self.head_node.nt.prev = self.cache_map[key]
            self.head_node.nt = self.cache_map[key]
            self.size += 1
            if (self.size > self.capacity):
                # remove LRU key
                LRU_key = self.tail_node.prev.key
                self.tail_node.prev.prev.nt = self.tail_node
                self.tail_node.prev = self.tail_node.prev.prev
                del self.cache_map[LRU_key]