# 方法1：每次 add 后重新排序
# 直接维护所有数字，每次重新排序后返回倒数第 k 个


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums[:]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8

    print("all tests passed")
