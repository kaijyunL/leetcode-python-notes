# 方法1：直接用数组模拟

import random


class RandomizedSet:
    def __init__(self):
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False
        self.nums.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


if __name__ == "__main__":
    randomized_set = RandomizedSet()

    assert randomized_set.insert(1) is True
    assert randomized_set.insert(1) is False
    assert randomized_set.insert(2) is True
    assert randomized_set.remove(3) is False
    assert randomized_set.remove(1) is True
    assert randomized_set.insert(2) is False

    value = randomized_set.getRandom()
    assert value == 2

    print("all tests passed")
