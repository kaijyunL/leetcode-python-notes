# 方法3：固定大小小顶堆（面试主推）
# 堆里始终保留当前最大的 k 个数，堆顶就是第 k 大

from heapq import heappop, heappush


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []

        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > self.k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8

    kth = KthLargest(1, [])
    assert kth.add(-3) == -3
    assert kth.add(-2) == -2
    assert kth.add(-4) == -2
    assert kth.add(0) == 0
    assert kth.add(4) == 4

    print("all tests passed")
