# 方法3：双堆 / 对顶堆（面试主推）
# small 是左半边最大堆（用负数模拟），large 是右半边最小堆
# addNum O(log n)，findMedian O(1)，空间 O(n)

from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))

        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    finder = MedianFinder()
    finder.addNum(1)
    assert finder.findMedian() == 1.0
    finder.addNum(2)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2.0

    finder = MedianFinder()
    for num, expected in [(5, 5.0), (15, 10.0), (1, 5.0), (3, 4.0)]:
        finder.addNum(num)
        assert finder.findMedian() == expected

    print("all tests passed")
