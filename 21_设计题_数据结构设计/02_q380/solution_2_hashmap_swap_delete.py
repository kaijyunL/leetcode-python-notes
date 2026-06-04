# 方法2：数组 + 哈希表记录下标（面试主推）

import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        remove_index = self.index_map[val]
        last_val = self.nums[-1]

        self.nums[remove_index] = last_val
        self.index_map[last_val] = remove_index

        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


if __name__ == "__main__":
    randomized_set = RandomizedSet()

    assert randomized_set.insert(1) is True
    assert randomized_set.remove(2) is False
    assert randomized_set.insert(2) is True

    value = randomized_set.getRandom()
    assert value in {1, 2}

    assert randomized_set.remove(1) is True
    assert randomized_set.insert(2) is False
    assert randomized_set.getRandom() == 2

    assert randomized_set.remove(2) is True
    assert randomized_set.insert(3) is True
    assert randomized_set.insert(4) is True
    assert randomized_set.remove(3) is True
    assert randomized_set.getRandom() == 4

    print("all tests passed")
