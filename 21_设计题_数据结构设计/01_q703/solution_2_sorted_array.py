# 方法2：维护有序数组
# 插入时用二分找位置，数组始终保持有序

from bisect import insort


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[-self.k]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8

    print("all tests passed")
