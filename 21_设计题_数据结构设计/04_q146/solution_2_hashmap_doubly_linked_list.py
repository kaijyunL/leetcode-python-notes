# 方法2：哈希表 + 双向链表（面试主推）

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def _remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node) -> None:
        last_node = self.dummy_tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.dummy_tail
        self.dummy_tail.prev = node

    def _move_to_tail(self, node: Node) -> None:
        self._remove_node(node)
        self._add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_tail(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)

        if len(self.cache) > self.capacity:
            lru_node = self.dummy_head.next
            self._remove_node(lru_node)
            del self.cache[lru_node.key]


if __name__ == "__main__":
    lru_cache = LRUCache(2)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1

    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1

    lru_cache.put(4, 4)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4

    lru_cache = LRUCache(2)
    lru_cache.put(2, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(2) == 2
    lru_cache.put(1, 1)
    lru_cache.put(4, 1)
    assert lru_cache.get(2) == -1

    print("all tests passed")
