# 方法2：维护有序数组
# 用 bisect.insort 把新数字插入正确位置；查询中位数 O(1)
# addNum O(n)，findMedian O(1)，空间 O(n)

from bisect import insort


class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(self.nums, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2

        if n % 2 == 1:
            return float(self.nums[mid])
        return (self.nums[mid - 1] + self.nums[mid]) / 2.0


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
