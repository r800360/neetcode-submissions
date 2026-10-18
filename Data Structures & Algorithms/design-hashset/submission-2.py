class MyHashSet:

    def __init__(self):
        self.hset = [0] * 1000001

    def add(self, key: int) -> None:
        if key < 0 or key > 1000000:
            return
        self.hset[key] = 1

    def remove(self, key: int) -> None:
        if key < 0 or key > 1000000:
            return
        self.hset[key] = 0

    def contains(self, key: int) -> bool:
        if key < 0 or key > 1000000:
            return False
        return self.hset[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)