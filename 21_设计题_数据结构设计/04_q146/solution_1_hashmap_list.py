# 方法1：哈希表 + 列表维护顺序

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache) == self.capacity:
            lru_key = self.order.pop(0)
            del self.cache[lru_key]

        self.cache[key] = value
        self.order.append(key)


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

    lru_cache.put(4, 40)
    assert lru_cache.get(4) == 40

    print("all tests passed")
